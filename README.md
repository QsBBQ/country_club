# country_club
Coding practice Country club member management

Working on a country club I have been tasked with tracking members. Instead of using a spreadsheet I have decided to create a app to do it! The chosen tech for the job python3.4.3 w/flask and sqlalchemy w/alembic and jquery/twitter bootstrap.


1. Some background
The country club has locations in Miami, Los Angeles and Houston and is growing. A Member and his family have access to the subscribed clubs. A member could live in multiple residences and multiple children.

* Initial db_Model
Tables
Location

Administrator
Member
  Could have many residences
  Could belong to many clubs
Family
  Belongs to one member
Club
  Club has one location
  Club has many members
Member_Location join table
  address
All_clubs join table
