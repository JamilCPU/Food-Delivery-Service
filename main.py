import User
import Authentication
import Store
import Driver
import Order

##Create User object and test getters
aUser = User.User("demo_user", "demo-pass", "Demo", "User", 5550100, "user@example.com")
print(aUser.getUsername(), "\n", aUser.getPassword(),
      aUser.getfName(), "\n", aUser.getlName(),
      aUser.getphoneNum(), "\n", aUser.getEmail())##test user methods

aUser.setEmail("user2@example.com")
aUser.setPassword("demo-pass-2")
aUser.setPhoneNum(5550101)
aUser.setUsername("demo_user2")