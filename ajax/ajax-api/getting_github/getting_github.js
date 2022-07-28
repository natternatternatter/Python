async function getCoderData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    console.log("button clicked")
    var response = await fetch("https://api.github.com/users/natternatternatter");
    console.log("response sent")
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    console.log("json recieved");
    console.log(coderData);

    document.querySelector("#githubInfo").innerHTML = coderData.login;

    return coderData;
}
    
console.log(getCoderData());