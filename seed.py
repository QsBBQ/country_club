from models import db_session, Club, Member, FamilyMember, MemberClubJoin

# Faker factory import
from faker import Factory
faker = Factory.create()

s = db_session()

# Clean up
for join in s.query(MemberClubJoin).all():
    s.delete(join)
for clubs in s.query(Club).all():
    s.delete(clubs)
for members in s.query(Member).all():
    s.delete(members)
for family_members in s.query(FamilyMember).all():
    s.delete(family_members)
s.commit()

# Adding Clubs

for i in range(1, 6):
    club = Club(name="club"+str(i),
                description="Beautiful club" + str(i)
                )
    for i in range(1, 6):
        member = Member(name=faker.name(),
                        username=faker.user_name()
                        )
        for i in range(3):
            if i == 0:
                familymember = FamilyMember(name=faker.name(),
                                            relation="wife",
                                            member_id=member.id)
                s.add(familymember)
                s.commit()
            else:
                familymember = FamilyMember(name=faker.name(),
                                            relation="kids",
                                            member_id=member.id)
                s.add(familymember)
                s.commit()
        s.add(member)
        s.commit()
        member_join = MemberClubJoin(club=club,
                                     member=member,
                                     tag="Legacy club member")
    s.add(club)
    s.commit()
