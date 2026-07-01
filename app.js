const state = {
  site: null,
  activeSlug: null,
};

const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");

function slugFromHash() {
  try {
    return decodeURIComponent(location.hash.replace(/^#/, ""));
  } catch {
    return "";
  }
}

function sectionBySlug(slug) {
  return state.site.sections.find((section) => section.slug === slug);
}

function setActiveNav(slug) {
  document.querySelectorAll(".nav-item").forEach((item) => {
    const isActive = item.dataset.slug === slug;
    item.classList.toggle("active", isActive);
    if (isActive) {
      item.setAttribute("aria-current", "page");
      return;
    }
    item.removeAttribute("aria-current");
  });
}

function renderNavigation() {
  sidebar.replaceChildren();

  state.site.sections.forEach((section) => {
    const link = document.createElement("a");
    link.className = "nav-item";
    link.href = `#${encodeURIComponent(section.slug)}`;
    link.dataset.slug = section.slug;
    link.textContent = section.label;
    link.addEventListener("click", (event) => {
      event.preventDefault();
      selectSection(section.slug, { updateHash: true });
    });
    sidebar.appendChild(link);
  });
}

function createMediaElement(item) {
  if (item.type === "video") {
    const video = document.createElement("video");
    video.src = item.src;
    video.controls = true;
    video.preload = "metadata";
    video.setAttribute("aria-label", item.alt);
    return video;
  }

  const image = document.createElement("img");
  image.src = item.src;
  image.alt = item.alt;
  image.loading = "lazy";
  image.decoding = "async";
  return image;
}

function renderSection(section) {
  const stack = document.createElement("div");
  stack.className = "media-stack";

  section.media.forEach((item) => {
    const figure = document.createElement("figure");
    figure.className = "media-frame";
    figure.appendChild(createMediaElement(item));
    stack.appendChild(figure);
  });

  content.replaceChildren(stack);
  content.focus({ preventScroll: true });
}

function selectSection(slug, options = {}) {
  const section = sectionBySlug(slug) || state.site.sections[0];
  state.activeSlug = section.slug;

  if (options.updateHash && location.hash !== `#${section.slug}`) {
    history.pushState(null, "", `#${section.slug}`);
  }

  setActiveNav(section.slug);
  renderSection(section);
  window.scrollTo({ top: 0, behavior: "auto" });
}

async function loadSite() {
  try {
    const response = await fetch("data/site.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`manifest request failed: ${response.status}`);
    }

    state.site = await response.json();
    renderNavigation();
    selectSection(slugFromHash() || state.site.sections[0].slug, { updateHash: false });
  } catch (error) {
    content.replaceChildren();
    const message = document.createElement("p");
    message.className = "error";
    message.textContent = "자료를 불러오지 못했습니다.";
    content.appendChild(message);
    console.error(error);
  }
}

window.addEventListener("hashchange", () => {
  if (!state.site) {
    return;
  }
  selectSection(slugFromHash(), { updateHash: false });
});

loadSite();
