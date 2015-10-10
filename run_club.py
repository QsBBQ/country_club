from flask import Flask, session, render_template, request, redirect

from models import db_session, Club, Member, FamilyMember, MemberClubJoin

s = db_session()

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)
