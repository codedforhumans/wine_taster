// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyArxjAy9WhiCu99lAODoN1BJdAnI1IbzLg",
  authDomain: "vyn-taster.firebaseapp.com",
  projectId: "vyn-taster",
  storageBucket: "vyn-taster.appspot.com",
  messagingSenderId: "10759210693",
  appId: "1:10759210693:web:5df7e74247f6e9016c12ac",
  measurementId: "G-LR742NW3TC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);