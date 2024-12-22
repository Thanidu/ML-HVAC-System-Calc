function submitForm(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('chillerForm'));

    fetch('', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            document.getElementById("outputTemp").textContent = data.output_temp;
            document.getElementById("evaporatorDuty").textContent = data.evaporator_duty;
            document.getElementById("generatorOutput").textContent = data.generator_output;
            document.getElementById("cop").textContent = data.cop;
        }
    })
    .catch(error => console.error("Error:", error));
}