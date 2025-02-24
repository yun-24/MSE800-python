document.getElementById('alertBtn')?.addEventListener('click', function() {
    alert('Hello from JavaScript!');
});

document.getElementById('helloBtn')?.addEventListener('click', function() {
    confirm("world")
});

document.getElementById('homeBtn')?.addEventListener('click', function() {
    window.location.href = "/"
});

let num = 0;
document.getElementById('changeBtn')?.addEventListener('click', function () {
    const list = [
        "https://images.ctfassets.net/fiyflsm3oqjv/t76wFyJ2BmUKiaU5sN6bO/1ce142f14b596184456eba5af4b8547c/IT-Hero-ImageC.jpg",
        "https://images.ctfassets.net/fiyflsm3oqjv/3OmZ7c6cf1CUFgMQ4MDFjD/9a861fea45cfa53f709d511c6d07fbf2/businessman-analyzing-company-financial-cash-flow-2023-11-27-05-22-21-utc__1_.jpg"]

    document.getElementById("image").src = list[num++ % list.length]
});

document.getElementById('imageInput').addEventListener('change', function(e) {
    const file = e.target.files[0];

    document.getElementById("image").src = URL.createObjectURL(file);
});
