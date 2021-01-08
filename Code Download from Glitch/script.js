// Your web app's Firebase configuration
// Your web app's Firebase configuration
const firebaseConfig = {
        apiKey: "AIzaSyDzNU5h7b7pWEB8jX4PftgRUBxsbeHtE6c",
        authDomain: "tomato-view.firebaseapp.com",
        databaseURL: "https://tomato-view-default-rtdb.firebaseio.com",
        projectId: "tomato-view",
        storageBucket: "tomato-view.appspot.com",
        messagingSenderId: "229766163619",
        appId: "1:229766163619:web:6a2c71b64fac2d269c2316"
};

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function(url) {
        console.log(url);
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function(error) {
        console.log(error);
      });
  });
});