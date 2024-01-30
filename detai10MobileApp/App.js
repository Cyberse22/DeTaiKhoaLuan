import { createDrawerNavigator } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native";
import Home from "./Components/Home/Home";

const Drawer = createDrawerNavigator

const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen name = "Home" componet={ Home }> </Drawer.Screen>
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

