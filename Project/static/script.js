function filterItems() {
    const categoryFilter = document.getElementById('category').value;
    const items = document.querySelectorAll('.item');

    items.forEach(item => {
        const category = item.dataset.category;
        let showItem = true;

        if (categoryFilter !== 'all' && categoryFilter !== category) {
            showItem = false;
        }

        if (showItem) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}