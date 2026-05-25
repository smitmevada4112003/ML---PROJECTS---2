    function predict() {
        let exp = document.getElementById("exp").value;
        let loading = document.getElementById("loading");
        let result = document.getElementById("result");
        let box = document.getElementById("outputBox");

        if (exp === "") {
            alert("Please enter experience!");
            return;
        }

        loading.classList.remove("hidden");
        box.classList.add("hidden");

        // 🔥 API call (model se connect)
        fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                YearExperience: parseFloat(exp)
            })
        })
        .then(res => res.json())
        .then(data => {
            loading.classList.add("hidden");

            result.innerText = "💰 ₹ " + data.predictSalary;

            // ✅ Niche output show
            box.classList.remove("hidden");
        })
        .catch(err => {
            loading.classList.add("hidden");
            result.innerText = "❌ Server error";
            box.classList.remove("hidden");
            console.error(err);
        });
    }