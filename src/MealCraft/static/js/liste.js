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
                        image: product["image_url"],
                        name: product["product_name"],
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

            var addButton = document.createElement("button");
            addButton.className = 'ajouter-button';
            
            // Créez un élément <i> pour l'icône de l'étoile de Font Awesome
            var starIcon = document.createElement("i");
            starIcon.className = 'fa-regular fa-star'; // Assurez-vous que la classe est correcte

            addButton.appendChild(starIcon); // Ajoutez l'icône de l'étoile à addButton

            addButton.addEventListener('click', function () {
                // Code pour basculer entre les classes CSS
                if (starIcon.className === 'fa-regular fa-star') {
                    starIcon.className = 'fa-solid fa-star';
                } else {
                    starIcon.className = 'fa-regular fa-star';
                }

                // Ajoutez ici le code pour gérer l'ajout de l'aliment
                // Vous pouvez utiliser food.name, food.image ou d'autres données de food
                alert('Vous avez ajouté : ' + food.name);
            });

            listItem.appendChild(addButton);
            resultList.appendChild(listItem);
        });
        resultContainer.appendChild(resultList);
    } else {
        resultContainer.textContent = "Aucun résultat trouvé.";
    }
}

