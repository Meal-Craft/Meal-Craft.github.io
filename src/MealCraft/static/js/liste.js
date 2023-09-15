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
                if ("product_name" in product && "image_url" in product) {
                    var food = {
                        name: product["product_name"],
                        image: product["image_url"],
                    };
                    uniqueFoods.push(food);
                }
            }

            return uniqueFoods;
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
        resultList.className = 'affichageResultat';
        uniqueFoods.forEach(function (food) {
            var listItem = document.createElement("li");
            listItem.className = 'card';

            var foodImage = document.createElement("img");
            foodImage.src = food.image;
            listItem.appendChild(foodImage);

            var foodName = document.createElement("span");
            foodName.classList.add('text');
            // couper le dernier mot du text si il est supérieur à 17 caractère
            if (food.name.length > 15) {
                food.name = food.name.substring(0, 15) + '...';
            }
            foodName.textContent = food.name;
            listItem.appendChild(foodName);

            resultList.appendChild(listItem);
        });
        resultContainer.appendChild(resultList);
    } else {
        resultContainer.textContent = "Aucun résultat trouvé.";
    }
}