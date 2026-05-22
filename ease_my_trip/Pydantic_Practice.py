from pydantic import BaseModel,EmailStr

class User(BaseModel):
    id: int
    name: str = "John Doe"
    email: EmailStr

# Valid data works fine
user = User(id="1", email="test@examplecom") #here pydantic autometically type conversion. str convert to int.
print(user)


# Invalid data (e.g., id as a string that can't be an int) raises a ValidationError
# user = User(id="abc", email="test@example.com") 
