document.addEventListener("DOMContentLoaded", () =>
  document
    .querySelectorAll("section.project.clearfix")
    .forEach((projectSection) =>
      projectSection.addEventListener("keydown", (event) =>
        event.key === "Enter" || event.keyCode === 13
          ? projectSection.getElementsByClassName("project-link")[0].click()
          : null
      )
    )
);
