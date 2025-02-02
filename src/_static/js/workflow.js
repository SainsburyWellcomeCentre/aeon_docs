class WorkflowContainer {
    static cellCounter = 0;

    static escapeHtml(unsafe)
    {
        return unsafe
             .replace(/&/g, "&amp;")
             .replace(/</g, "&lt;")
             .replace(/>/g, "&gt;")
             .replace(/"/g, "&quot;")
             .replace(/'/g, "&#039;");
     }

    static createWorkflowCell(img, path) {
        const wrap = document.createElement("div");
        wrap.classList.add("highlight");

        // workflow SVG renders in a visible pre element
        const workflowCell = document.createElement("pre");
        wrap.appendChild(workflowCell);
        const imgParent = img.parentElement;
        workflowCell.appendChild(img);

        // remove the parent p element from custom .md containers
        if (imgParent.nodeName.toLowerCase() === "p") {
            imgParent.remove();
        }

        // set button SVG from sphinx-copybutton
        const id = "workflowcell" + WorkflowContainer.cellCounter++;
        const clipboardButton = id =>
        `<button class="copybtn o-tooltip--left" data-tooltip="${messages[locale]['copy']}" data-clipboard-target="#${id}">
        ${iconCopy}
        </button>`
        workflowCell.insertAdjacentHTML('afterend', clipboardButton(id))

        // fetch contents into an invisible pre for copying
        fetch(path).then(req => req.text()).then(contents => {
            const codeCell = document.createElement("pre");
            codeCell.id = id;
            codeCell.innerHTML = WorkflowContainer.escapeHtml(contents);
            codeCell.hidden = true;
            wrap.appendChild(codeCell);
        });
        return wrap;
    }

    static renderElement(element) {
        element.classList.add("highlight-bonsai");
        const img = element.querySelector("img");

        // assumes all workflow references are hosted in _workflows/
        const workflowPath = img.src
            .replace("_images/", "_workflows/")
            .replace(/\.[^.]+$/, ".bonsai");

        const wrap = WorkflowContainer.createWorkflowCell(img, workflowPath);
        const parent = element.parentElement;
        parent.insertBefore(wrap, element);
        element.appendChild(wrap);
    }
    
    static init() {
        const observer = new MutationObserver(() => {
            const theme = document.documentElement.getAttribute("data-bs-theme");
            const root = document.querySelector(':root');
            root.style.setProperty("color-scheme", theme);
        }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-bs-theme'] })
        for (const element of document.getElementsByClassName("workflow")) {
            WorkflowContainer.renderElement(element)
        }
    }
}

// reuse load function from sphinx-copybutton
runWhenDOMLoaded(WorkflowContainer.init);