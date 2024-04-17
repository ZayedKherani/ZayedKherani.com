// // mailchannels-worker.js
// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("contact-form");

//   form.addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent the default form submission

//     // Gather the data from the form
//     const name = document.getElementById("name").value;
//     const email = document.getElementById("email").value;
//     const subject = document.getElementById("subject").value;
//     const message = document.getElementById("message").value;

//     // Create the request payload
//     const payload = {
//       email: email,
//       name: name,
//       subject: subject,
//       message: message
//     };

//     // Send the data to the MailChannels worker
//     fetch("https://mainchannelworker.zayedkherani.com/", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify(payload)
//     })
//       .then((response) => {
//         if (response.ok) {
//           // Display a success message
//           alert("Message sent successfully!");
//           // Clear the form
//           form.reset();
//         } else {
//           // Handle errors
//           alert("Failed to send message. Please try again later.");
//         }
//       })
//       .catch((error) => {
//         console.error("There was an error sending the message:", error);
//         alert("An error occurred. Please try again later.");
//       });
//   });
// });

// mailchannels-worker.js
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather the data from the form
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    // Create the request payload
    const payload = {
      email: email,
      name: name,
      subject: subject,
      message: message
    };

    // Send the data to the MailChannels worker
    fetch("https://mainchannelworker.zayedkherani.com/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: payload
    })
      .then((response) => {
        if (response.ok) {
          // Display a success message
          alert("Message sent successfully!");
          // Clear the form
          form.reset();
        } else {
          // Handle errors
          alert("Failed to send message. Please try again later.");
        }
      })
      .catch((error) => {
        console.error("There was an error sending the message:", error);
        alert("An error occurred. Please try again later.");
      });
  });
});
