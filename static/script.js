document.getElementById("submit-code").addEventListener("click", function () {
  var userCode = document.getElementById("user-code").value;
  fetch("/improve-code", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code: userCode }),
  })
    .then((response) => response.json())
    .then((data) => {
      var formattedText = data.improved_code;

      // Wrap text in pre tags to preserve newlines
      formattedText = "<pre>" + formattedText + "</pre>";

      // Replace Markdown code block syntax with HTML tags
      formattedText = formattedText
        .replace(/```python/g, "<code>")
        .replace(/```/g, "</code>");

      // Update the llm-output element with the formatted text
      var outputDiv = document.getElementById("llm-output");
      outputDiv.innerHTML = formattedText;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
// Double click to select entire text input box
document
  .getElementById("user-code")
  .addEventListener("dblclick", function (event) {
    event.target.select();
  });
