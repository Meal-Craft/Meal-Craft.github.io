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
                        id: product["code"],
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
    location.replace("/#")
    var searchQuery = document.getElementById("searchInput").value;
    var uniqueFoods = getUniqueFoods(searchQuery);

    var resultContainer = document.getElementById("resultContainer");
        
    while (resultContainer.firstChild) { resultContainer.removeChild(resultContainer.firstChild); }
    
    if (uniqueFoods.length > 0) {         
        var resultList = document.createElement("ul");
        resultList.className = 'affichageResultat';
        uniqueFoods.forEach(function (food) {
            var listItem = document.createElement("li");
            listItem.className = 'card';



            var foodImage = document.createElement("img");
            foodImage.src = food.image;
            listItem.appendChild(foodImage);
            foodImage.addEventListener('click', function () {
                location.replace("/food/" + food.id)

            });

            var addButton = document.createElement("button");
            addButton.className = 'ajouter-button';
            
            // Créez un élément <i> pour l'icône de l'étoile de Font Awesome
            var starIcon = document.createElement("i");
            starIcon.className = 'fa-regular fa-star';
            for (let i = 0; i < liste.length; i++) {
                if (liste[i]["fields"]["nutrimcode"] === food.id) {
                    starIcon.className = 'fa-solid fa-star';
                    break;
                }
            }


            if (logged) {
                addButton.appendChild(starIcon);
                addButton.addEventListener('click', function () {
                    if (starIcon.className === 'fa-regular fa-star') {
                        starIcon.className = 'fa-solid fa-star';
                    } else {
                        starIcon.className = 'fa-regular fa-star';
                    }

                });

            
                listItem.appendChild(addButton);
            }
            resultList.appendChild(listItem);
        });
        resultContainer.appendChild(resultList);
    } else {
        resultContainer.textContent = "Aucun résultat trouvé.";
    }
}

