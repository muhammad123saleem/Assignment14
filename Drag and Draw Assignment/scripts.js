const dragItem = document.getElementById("dragMe");
    const boxes = document.querySelectorAll(".box");

    // When drag starts
    dragItem.addEventListener("dragstart", (e) => {
      e.dataTransfer.setData("text/plain", e.target.id);
    });

    // Prevent default on dragover to allow drop
    boxes.forEach(box => {
      box.addEventListener("dragover", (e) => {
        e.preventDefault();
      });

      // Handle drop
      box.addEventListener("drop", (e) => {
        e.preventDefault();
        const data = e.dataTransfer.getData("text/plain");
        const draggedElement = document.getElementById(data);
        box.appendChild(draggedElement);
      });
    });