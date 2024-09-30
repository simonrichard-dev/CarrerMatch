import React from 'react';
import { View, Text, TouchableOpacity, Image, StyleSheet } from 'react-native';

const LoginScreen = () => {
  const handleEmailLogin = () => {
    // Logique pour la connexion par email/mot de passe
  };

  const handleSocialLogin = (provider: string) => {
    // Logique pour la connexion via Google, GitHub ou LinkedIn
    console.log(`Connexion avec ${provider}`);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Connexion</Text>

      {/* Connexion par email */}
      <TouchableOpacity style={styles.button} onPress={handleEmailLogin}>
        <Text style={styles.buttonText}>Connexion avec Email</Text>
      </TouchableOpacity>

      {/* Connexion sociale */}
      <Text style={styles.orText}>ou</Text>
      <View style={styles.socialButtonsContainer}>
        <TouchableOpacity onPress={() => handleSocialLogin('Google')}>
          <Image source={require('../assets/icons/Google.png')} style={styles.icon} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => handleSocialLogin('GitHub')}>
          <Image source={require('../assets/icons/Github.png')} style={styles.icon} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => handleSocialLogin('LinkedIn')}>
          <Image source={require('../assets/icons/LinkedIn.png')} style={styles.icon} />
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#007BFF', // Couleur du bouton
    padding: 10,
    borderRadius: 5,
    width: '80%',
    alignItems: 'center',
    marginBottom: 10,
  },
  buttonText: {
    color: '#FFFFFF', // Couleur du texte
    fontSize: 18,
  },
  orText: {
    marginVertical: 10,
    fontSize: 16,
  },
  socialButtonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '80%',
  },
  icon: {
    width: 40,
    height: 40,
  },
});

export default LoginScreen;
