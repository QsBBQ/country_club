from flask import Flask, session, render_template, request, redirect

from models import db_session, Club, Member, FamilyMember, MemberClubJoin

s = db_session()

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def hello():
    clubs = s.query(Club).order_by(Club.name).all()

    return render_template("index.html",
                           clubs=clubs)


@app.route("/member/<int:member_id>")
def member(member_id):
    clubs = s.query(Club).order_by(Club.name).all()
    member = s.query(Member).filter(Member.id == member_id).first()
    return render_template("members_display.html",
                           clubs=clubs,
                           member=member)


@app.route("/member/<int:member_id>/edit", methods=['GET', 'POST'])
def member_edit(member_id):
    clubs = s.query(Club).order_by(Club.name).all()
    member = s.query(Member).filter(Member.id == member_id).first()
    if request.method == 'POST':
        post_data = request.form
        # print(post_data)
        member_name = request.form["member_name"]
        member_username = request.form["member_username"]
        member_note = request.form["member_note"]
        member.name = member_name
        member.username = member_username
        member.note = member_note
        s.commit()
        for form_key in post_data.keys():
            # print(form_key)
            # need to review if this makes sense
            if "family" in form_key:
                family_member_id = form_key.split()[1]
                family_member = s.query(FamilyMember).filter(FamilyMember.id == family_member_id).first()
                if "family_member_name":
                    family_member_name = request.form[form_key]
                    family_member.name = family_member_name
                if "family_member_relation":
                    family_member_relation = request.form[form_key]
                    family_member.relation = family_member_relation
            # This should be changed to a list of available clubs and this members membership
            if "club" in form_key:
                club_id = form_key.split()[1]
                club_query = s.query(Club).filter(Club.id == club_id).first()
                club_name = request.form[form_key]
                club_query.name = club_name
        return redirect("/member/{}".format(member_id))

    return render_template("member_edit.html",
                           clubs=clubs,
                           member=member)

@app.route("/member/<int:member_id>/delete", methods=['GET', 'POST'])
def member_delete(member_id):
    clubs = s.query(Club).order_by(Club.name).all()
    member = s.query(Member).filter(Member.id == member_id).first()
    return render_template("member_delete.html",
                           clubs=clubs,
                           member=member)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)
