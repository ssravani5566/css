// Select all grid items
const gridItems = document.querySelectorAll('.container > div');

// Add a click event listener to each item
gridItems.forEach(item => {
  item.addEventListener('click', function() {
    // Remove the 'highlighted' class from all items
    gridItems.forEach(i => i.classList.remove('highlighted'));
    
    // Add the 'highlighted' class to the clicked item
    this.classList.add('highlighted');
  });
});
