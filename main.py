import User
import Authentication
import Store
import Driver
import Order

##Create User object and test getters
aUser = User.User("tomjones", "00023", "tom", "jones", 5551359502, "tomjones00023@gmail.com")
print(aUser.getUsername(), "\n", aUser.getPassword(),
      aUser.getfName(), "\n", aUser.getlName(),
      aUser.getphoneNum(), "\n", aUser.getEmail())##test user methods

aUser.setEmail("00023jonestom@gmail.com")
aUser.setPassword("32000")
aUser.setPhoneNum(2059531555)
aUser.setUsername("jonestom")