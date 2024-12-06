let stars = ["star1", "star2", "star3", "star4", "star5"];
// document.getElementById("stars_value").value = "1";
// document.getElementById("star2").style.color = "red";

changeStar(1);

function changeStar(value) {
    document.getElementById("stars_value").value = value;
    for (let i = value; i < 5; i++) {
        document.getElementById(stars[i]).style.color = "gray";
    }
    for (let i = 0; i < value; i++) {
        document.getElementById(stars[i]).style.color = "gold";
    }
}