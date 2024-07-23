// Simulated Search feature
document.addEventListener("DOMContentLoaded", function () {
  const searchQuery = getSearchQuery();
  const resultsContainer = document.getElementById("results-container");

  // Defines the keywords that redirect to services.html
  const redirectKeywords = [
    "handyman",
    "Home Repairs",
    "Carpentry",
    "Painting",
  ];

  // Secondary keywords for different results
  const generalWords = ["Commitment", "About"];

  if (redirectKeywords.includes(searchQuery)) {
    // Will go to services.html for specific keywords
    window.location.href = "services.html";
  } else if (generalWords.includes(searchQuery)) {
    // Will go to about.html for specific keywords
    window.location.href = "about.html";
  } else {
    // No results found (or redirect to an error page)
    resultsContainer.innerHTML =
      "<p>Sorry, no results found for your search query.</p>";
  }
});

function getSearchQuery() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get("q");
}

// Star Rating Sytem
$(document).ready(function () {
  // This function handles the behavior when a star is hovered over
// This function handles the behavior when a star is hovered over
function handleStarHover() {
  const rating = $(this).data("rating");
  $(this).closest(".provider").find(".rating-value").text(rating);

  // Add the "active" class to the selected star and stars before it
  $(this).prevAll().addBack().addClass("active");  // Ensure this line is correct
  // Remove the "active" class from stars after the selected one
  $(this).nextAll().removeClass("active");
}

// When hovering over a star, handle the hover behavior and update the rating value
$(document).ready(function () {
  $(".star").hover(handleStarHover, function () {
    // Get the current rating value displayed in the provider section
    const currentRating = $(this).closest(".provider").find(".rating-value").text();

    // Remove the "active" class from all stars and restore the current rating value
    $(this).closest(".provider").find(".stars span").removeClass("active");
    $(this).closest(".provider").find(".rating-value").text(currentRating);
  });
});

// Ensure this part is outside of the $(document).ready to ensure it's globally available if not already
$(document).ready(function () {
    $(".star").hover(handleStarHover, function () {
        const currentRating = $(this).closest(".provider").find(".rating-value").text();
        $(this).closest(".provider").find(".stars span").removeClass("active");
        $(this).closest(".provider").find(".rating-value").text(currentRating);
    });
});



  // When hovering over a star, handle the hover behavior and update the rating value
  $(".star").hover(handleStarHover, function () {
    // Get the current rating value displayed in the provider section
    const currentRating = $(this)
      .closest(".provider")
      .find(".rating-value")
      .text();

    // Remove the "active" class from all stars and restore the current rating value
    $(this).closest(".provider").find(".stars span").removeClass("active");
    $(this).closest(".provider").find(".rating-value").text(currentRating);
  });

  // When a star is clicked, update the displayed rating value
  $(".star").click(function () {
    const rating = $(this).data("rating"); // Get the rating value from the star's data attribute
    $(this).closest(".provider").find(".rating-value").text(rating);
  });
});

// Schedule Appointment Feature
$(document).ready(function () {
  // Submit the appointment form
  $("#appointment-form").submit(function (event) {
    event.preventDefault();
    // Get entered service, date, and time
    const enteredService = $("#service").val();
    const selectedDate = $("#date").val();
    const selectedTime = $("#time").val();

    // Validate that the service input is not empty
    if (enteredService.trim() === "") {
      alert("Please enter a service.");
      return; // Stop the form submission if service is empty
    }

    // We will alert the data return here with the entered data
    alert(
      `Appointment Scheduled\nService: ${enteredService}\nDate: ${selectedDate}\nTime: ${selectedTime}`
    );

    // Clear the form fields after submission
    $("#service").val("");
    $("#date").val("");
    $("#time").val("");
  });
});
