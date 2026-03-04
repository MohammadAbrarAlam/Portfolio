async function sendMessage() {
    let input = document.getElementById("msg");
    let message = input.value;

    let res = await fetch("/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    let data = await res.json();
    document.getElementById("messages").innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
    input.value = "";
}