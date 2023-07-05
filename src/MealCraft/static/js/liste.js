function getUniqueFoods(searchQuery) {
  var apiURL =
    "https://world.openfoodfacts.org/cgi/search.pl?search_terms=" +
    encodeURIComponent(searchQuery) +
    "&search_simple=1&action=process&json=1";

  var xhr = new XMLHttpRequest();
  xhr.open("GET", apiURL, false);
  xhr.send();

  if (xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);

    if ("products" in data) {
      var products = data["products"];
      var uniqueFoods = [];

      for (var i = 0; i < products.length; i++) {
        var product = products[i];
        if ("product_name" in product) {
          uniqueFoods.push(product["product_name"]);
        }
      }

      return Array.from(new Set(uniqueFoods));
    }
  }

  return [];
}

function search() {
  var searchQuery = document.getElementById("searchInput").value;
  var uniqueFoods = getUniqueFoods(searchQuery);

  var resultContainer = document.getElementById("resultContainer");
  resultContainer.innerHTML = "";

  if (uniqueFoods.length > 0) {
    var resultList = document.createElement("ul");
    uniqueFoods.forEach(function (food) {
      var listItem = document.createElement("li");
      listItem.textContent = food;
      resultList.appendChild(listItem);
    });
    resultContainer.appendChild(resultList);
  } else {
    resultContainer.textContent = "Aucun résultat trouvé.";
  }
}
