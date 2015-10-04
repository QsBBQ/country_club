# how to get this working as package?
# from country_club.db import db_session
# from country_club.models import #import tables
from models import db_session, Club, Member, FamilyMember, MemberClubJoin

s = db_session()

# delete tables
for join in s.query(MemberClubJoin).all():
    s.delete(join)
for clubs in s.query(Club).all():
    s.delete(clubs)
for members in s.query(Member).all():
    s.delete(members)
for family_members in s.query(FamilyMember).all():
    s.delete(family_members)
s.commit()

print("Clean tables Club, Member, FamilyMember")
print(s.query(Club).count() == 0)
print(s.query(Member).count() == 0)
print(s.query(FamilyMember).count() == 0)
print(s.query(MemberClubJoin).count() == 0)

# Club test
club1 = Club(name="club1",
             description="Beautiful club1"
             )
s.add(club1)
s.commit()
print("****")
print("Club1 added")
print(s.query(Club).count() == 1)
print(s.query(Club).filter(Club.name == "club1").first().name == "club1")

# Member test
member1 = Member(name="member1",
                 username="member1"
                 )
s.add(member1)
s.commit()
print("****")
print("Member1 added")
print(s.query(Member).count() == 1)
print(s.query(Member).filter(Member.name == "member1").first().name == "member1")

# Family Member test
familymember1 = FamilyMember(name="jlo",
                             relation="wife",
                             member_id=member1.id
                             )
s.add(familymember1)
s.commit()
print("****")
print("Family Member added with relation to member1")
print(s.query(FamilyMember).count() == 1)
print(s.query(FamilyMember).filter(FamilyMember.name == "jlo").first().name == "jlo")
print(familymember1.members.name == "member1")

# Members to club
member_join = MemberClubJoin(club=club1,
                             member=member1,
                             tag="First club member!")
s.add(member_join)
s.commit()
print("")
