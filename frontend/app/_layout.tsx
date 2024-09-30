import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="login" options={{ title: 'Connexion' }} />
      <Stack.Screen name="home" options={{ title: 'Accueil' }} />
      <Stack.Screen name="profile" options={{ title: 'Profil' }} />
    </Stack>
  );
}
