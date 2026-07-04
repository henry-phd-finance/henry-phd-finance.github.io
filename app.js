const state = {
  site: null,
  activeSlug: null,
  activeVariantBySlug: {},
  activeInlineBySlug: {},
};

const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");
const brand = document.getElementById("brand");
const mobileBrand = document.getElementById("mobile-brand");

function slugFromHash() {
  try {
    return decodeURIComponent(location.hash.replace(/^#/, ""));
  } catch {
    return "";
  }
}

function sectionBySlug(slug) {
  return state.site.sections.find(
    (section) => section.slug === slug || section.aliases?.includes(slug),
  );
}

function splitRoute(route) {
  const [slug = "", inlineSlug = ""] = route.split("/");
  return { slug, inlineSlug };
}

function inlineTargetForSection(section, targetSlug) {
  if (!targetSlug || !Array.isArray(section.links)) {
    return null;
  }

  const link = section.links.find((item) => item.targetSlug === targetSlug);
  if (!link) {
    return null;
  }

  return sectionBySlug(targetSlug) || null;
}

function parentSectionForInlineTarget(targetSlug) {
  if (!targetSlug) {
    return null;
  }

  return state.site.sections.find((section) =>
    section.links?.some((item) => item.targetSlug === targetSlug),
  ) || null;
}

function resolveRoute(rawRoute) {
  const defaultSection = state.site.sections[0];
  if (!rawRoute) {
    return { section: defaultSection, inlineSlug: null, replaceHash: false };
  }

  const { slug, inlineSlug } = splitRoute(rawRoute);
  const section = sectionBySlug(slug);

  if (section?.hiddenFromNav) {
    const parent = parentSectionForInlineTarget(section.slug);
    if (parent) {
      return {
        section: parent,
        inlineSlug: section.slug,
        replaceHash: true,
      };
    }
  }

  if (section) {
    const validInlineSlug = inlineTargetForSection(section, inlineSlug) ? inlineSlug : null;
    return {
      section,
      inlineSlug: validInlineSlug,
      replaceHash: Boolean(inlineSlug && !validInlineSlug),
    };
  }

  return { section: defaultSection, inlineSlug: null, replaceHash: true };
}

function hashForRoute(sectionSlug, inlineSlug = null) {
  const encodedSection = encodeURIComponent(sectionSlug);
  if (!inlineSlug) {
    return `#${encodedSection}`;
  }
  return `#${encodedSection}/${encodeURIComponent(inlineSlug)}`;
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

  brand.textContent = state.site.siteLabel;
  brand.href = `#${encodeURIComponent(state.site.sections[0].slug)}`;
  mobileBrand.textContent = state.site.siteLabel;

  state.site.sections.filter((section) => !section.hiddenFromNav).forEach((section) => {
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

function renderHeader(section) {
  const header = document.createElement("header");
  header.className = "section-header";

  const title = document.createElement("h1");
  title.textContent = section.title || section.label;
  header.appendChild(title);

  if (section.description) {
    const description = document.createElement("p");
    description.className = "section-description";
    description.textContent = section.description;
    header.appendChild(description);
  }

  if (Array.isArray(section.links) && section.links.length > 0) {
    const links = document.createElement("div");
    links.className = "section-links";
    section.links.forEach((item) => {
      if (item.targetSlug) {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = item.label;
        const isActive = state.activeInlineBySlug[section.slug] === item.targetSlug;
        button.classList.toggle("active", isActive);
        button.setAttribute("aria-pressed", String(isActive));
        button.addEventListener("click", () => {
          selectSection(`${section.slug}/${item.targetSlug}`, { updateHash: true });
        });
        links.appendChild(button);
        return;
      }

      const link = document.createElement("a");
      link.href = item.href;
      link.textContent = item.label;
      links.appendChild(link);
    });
    header.appendChild(links);
  }

  return header;
}

function createProfileLink(item) {
  if (!item.href) {
    return document.createTextNode(item.value);
  }

  const link = document.createElement("a");
  link.href = item.href;
  link.textContent = item.value;
  return link;
}

function renderProfile(profile) {
  const header = document.createElement("header");
  header.className = "profile-header";

  const name = document.createElement("h1");
  name.textContent = profile.name;
  header.appendChild(name);

  if (profile.headline) {
    const headline = document.createElement("p");
    headline.className = "profile-headline";
    headline.textContent = profile.headline;
    header.appendChild(headline);
  }

  if (Array.isArray(profile.contacts) && profile.contacts.length > 0) {
    const contacts = document.createElement("dl");
    contacts.className = "profile-meta";
    profile.contacts.forEach((item) => {
      const label = document.createElement("dt");
      label.textContent = item.label;

      const value = document.createElement("dd");
      value.appendChild(createProfileLink(item));

      contacts.appendChild(label);
      contacts.appendChild(value);
    });
    header.appendChild(contacts);
  }

  return header;
}

function activeVariantIndex(section) {
  const selected = state.activeVariantBySlug[section.slug] ?? 0;
  if (!Array.isArray(section.variants) || section.variants.length === 0) {
    return 0;
  }
  return Math.min(Math.max(selected, 0), section.variants.length - 1);
}

function activeVariant(section) {
  if (!Array.isArray(section.variants) || section.variants.length === 0) {
    return null;
  }
  return section.variants[activeVariantIndex(section)];
}

function renderVariantControls(section) {
  const controls = document.createElement("div");
  controls.className = "variant-controls";
  controls.setAttribute("role", "tablist");
  controls.setAttribute("aria-label", `${section.label} document language`);

  section.variants.forEach((variant, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "variant-button";
    button.textContent = variant.label;
    button.setAttribute("role", "tab");
    button.setAttribute("aria-selected", String(index === activeVariantIndex(section)));
    if (index === activeVariantIndex(section)) {
      button.classList.add("active");
    }
    button.addEventListener("click", () => {
      state.activeVariantBySlug[section.slug] = index;
      selectSection(section.slug, { updateHash: false });
    });
    controls.appendChild(button);
  });

  return controls;
}

function renderDocumentActions(section, variant) {
  const links = [];
  if (variant?.pdfSrc) {
    links.push({
      href: variant.pdfSrc,
      label: variant.pdfLabel || "PDF 다운로드",
    });
  }
  if (section.pdfSrc) {
    links.push({
      href: section.pdfSrc,
      label: section.pdfLabel || "PDF 다운로드",
    });
  }

  if (links.length === 0) {
    return null;
  }

  const actions = document.createElement("div");
  actions.className = "document-actions";
  links.forEach((item) => {
    const link = document.createElement("a");
    link.href = item.href;
    link.textContent = item.label;
    link.setAttribute("download", "");
    actions.appendChild(link);
  });

  return actions;
}

function renderBlocks(blocks = []) {
  const fragment = document.createDocumentFragment();

  blocks.forEach((block) => {
    if (block.type === "paragraph") {
      const paragraph = document.createElement("p");
      paragraph.className = "content-paragraph";
      paragraph.textContent = block.text;
      fragment.appendChild(paragraph);
      return;
    }

    if (block.type === "list") {
      const list = document.createElement("ul");
      list.className = "content-list";
      block.items.forEach((text) => {
        const item = document.createElement("li");
        item.textContent = text;
        list.appendChild(item);
      });
      fragment.appendChild(list);
    }
  });

  return fragment;
}

function renderMediaStack(media = []) {
  const stack = document.createElement("div");
  stack.className = "media-stack";

  media.forEach((item) => {
    const figure = document.createElement("figure");
    figure.className = "media-frame";
    figure.appendChild(createMediaElement(item));
    stack.appendChild(figure);
  });

  return stack;
}

function renderMediaGroups(mediaGroups = []) {
  const fragment = document.createDocumentFragment();

  mediaGroups.forEach((group) => {
    const section = document.createElement("section");
    section.className = "media-group";

    const heading = document.createElement("h2");
    heading.textContent = group.title;
    section.appendChild(heading);
    section.appendChild(renderMediaStack(group.media));

    fragment.appendChild(section);
  });

  return fragment;
}

function renderInlineTarget(section) {
  const targetSlug = state.activeInlineBySlug[section.slug];
  const target = inlineTargetForSection(section, targetSlug);
  if (!target) {
    return null;
  }

  const panel = document.createElement("section");
  panel.className = "inline-target-panel";
  panel.id = `inline-${target.slug}`;

  const title = document.createElement("h2");
  title.textContent = target.title || target.label;
  panel.appendChild(title);

  if (target.description) {
    const description = document.createElement("p");
    description.className = "section-description";
    description.textContent = target.description;
    panel.appendChild(description);
  }

  panel.appendChild(renderBlocks(target.blocks));

  if (Array.isArray(target.mediaGroups)) {
    panel.appendChild(renderMediaGroups(target.mediaGroups));
  }

  if (Array.isArray(target.media)) {
    panel.appendChild(renderMediaStack(target.media));
  }

  return panel;
}

function renderMarkdown(markdown, sectionSlug = "") {
  const container = document.createElement("article");
  container.className = "document";
  const lines = markdown.split(/\r?\n/);
  let index = 0;
  let projectGroup = "deep";
  let currentProjectCard = null;

  function appendInlineMarkdown(parent, text) {
    const pattern = /(\*\*[^*]+\*\*|`[^`]+`)/g;
    let lastIndex = 0;
    let match = pattern.exec(text);

    while (match) {
      if (match.index > lastIndex) {
        parent.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
      }

      const token = match[0];
      const element = token.startsWith("**")
        ? document.createElement("strong")
        : document.createElement("code");
      element.textContent = token.startsWith("**") ? token.slice(2, -2) : token.slice(1, -1);
      parent.appendChild(element);

      lastIndex = match.index + token.length;
      match = pattern.exec(text);
    }

    if (lastIndex < text.length) {
      parent.appendChild(document.createTextNode(text.slice(lastIndex)));
    }
  }

  function targetContainer() {
    return currentProjectCard || container;
  }

  function appendNode(node) {
    targetContainer().appendChild(node);
  }

  function appendParagraph(text) {
    const paragraph = document.createElement("p");
    appendInlineMarkdown(paragraph, text);
    appendNode(paragraph);
  }

  function splitLabelValue(text) {
    const boldMatch = text.match(/^\*\*([^*]+?)\s*:?\*\*\s*:?\s*(.+)$/);
    if (boldMatch) {
      return {
        label: boldMatch[1].replace(/:$/, "").trim(),
        value: boldMatch[2].trim(),
      };
    }

    const plainMatch = text.match(/^([^:：]{2,42}):\s+(.+)$/);
    if (!plainMatch) {
      return null;
    }

    return {
      label: plainMatch[1].trim(),
      value: plainMatch[2].trim(),
    };
  }

  function createInfoList(rows) {
    const list = document.createElement("dl");
    list.className = "info-list";

    rows.forEach(({ label, value }) => {
      const row = document.createElement("div");
      row.className = "info-row";

      const term = document.createElement("dt");
      term.textContent = label;

      const description = document.createElement("dd");
      appendInlineMarkdown(description, value);

      row.appendChild(term);
      row.appendChild(description);
      list.appendChild(row);
    });

    return list;
  }

  while (index < lines.length) {
    const line = lines[index];
    const trimmed = line.trim();

    if (!trimmed) {
      index += 1;
      continue;
    }

    if (trimmed.startsWith("|") && lines[index + 1]?.trim().startsWith("|")) {
      const tableLines = [];
      while (index < lines.length && lines[index].trim().startsWith("|")) {
        tableLines.push(lines[index].trim());
        index += 1;
      }
      const table = document.createElement("table");
      tableLines.forEach((tableLine, rowIndex) => {
        if (rowIndex === 1 && /^(\|\s*:?-{3,}:?\s*)+\|?$/.test(tableLine)) {
          return;
        }
        const row = document.createElement("tr");
        tableLine
          .split("|")
          .slice(1, -1)
          .forEach((cellText) => {
            const cell = document.createElement(rowIndex === 0 ? "th" : "td");
            cell.textContent = cellText.trim();
            row.appendChild(cell);
          });
        table.appendChild(row);
      });
      appendNode(table);
      continue;
    }

    const heading = trimmed.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      const level = heading[1].length === 1 ? 2 : Math.min(heading[1].length, 5);
      const element = document.createElement(`h${level}`);
      element.textContent = heading[2].trim();

      if (sectionSlug === "projects" && level === 2) {
        currentProjectCard = null;
        projectGroup = element.textContent.includes("Additional") ? "additional" : "deep";
        container.appendChild(element);
        index += 1;
        continue;
      }

      if (sectionSlug === "projects" && level === 3) {
        currentProjectCard = document.createElement("section");
        currentProjectCard.className = `project-card project-card-${projectGroup}`;
        currentProjectCard.appendChild(element);
        container.appendChild(currentProjectCard);
        index += 1;
        continue;
      }

      appendNode(element);
      index += 1;
      continue;
    }

    if (trimmed.startsWith("- ")) {
      if (sectionSlug === "projects" && currentProjectCard) {
        const details = document.createElement("dl");
        details.className = "project-details";

        while (index < lines.length && lines[index].trim().startsWith("- ")) {
          const detailText = lines[index].trim().replace(/^- /, "");
          const labelMatch = detailText.match(/^\*\*([^*]+)\*\*\s*(.*)$/);
          const row = document.createElement("div");
          row.className = "project-detail-row";

          if (labelMatch) {
            const term = document.createElement("dt");
            const label = labelMatch[1].replace(/:$/, "");
            term.textContent = label;

            const description = document.createElement("dd");
            if (label === "메타") {
              row.classList.add("project-detail-meta");
              description.className = "project-meta-tags";
              labelMatch[2].split("·").forEach((tagText) => {
                const trimmedTag = tagText.trim();
                if (!trimmedTag) {
                  return;
                }
                const tag = document.createElement("span");
                tag.className = "project-meta-tag";
                tag.textContent = trimmedTag;
                description.appendChild(tag);
              });
            } else {
              if (label === "결과") {
                row.classList.add("project-detail-impact");
              }
              appendInlineMarkdown(description, labelMatch[2]);
            }

            row.appendChild(term);
            row.appendChild(description);
          } else {
            const description = document.createElement("dd");
            description.className = "project-detail-unlabeled";
            appendInlineMarkdown(description, detailText);
            row.appendChild(description);
          }

          details.appendChild(row);
          index += 1;
        }

        appendNode(details);
        continue;
      }

      const itemTexts = [];
      while (index < lines.length && lines[index].trim().startsWith("- ")) {
        itemTexts.push(lines[index].trim().replace(/^- /, ""));
        index += 1;
      }

      const infoRows = itemTexts.map(splitLabelValue);
      if (infoRows.every(Boolean)) {
        appendNode(createInfoList(infoRows));
        continue;
      }

      const list = document.createElement("ul");
      itemTexts.forEach((itemText) => {
        const item = document.createElement("li");
        appendInlineMarkdown(item, itemText);
        list.appendChild(item);
      });
      appendNode(list);
      continue;
    }

    const paragraphLines = [];
    while (
      index < lines.length &&
      lines[index].trim() &&
      !lines[index].trim().startsWith("#") &&
      !lines[index].trim().startsWith("- ")
    ) {
      paragraphLines.push(lines[index].trim());
      index += 1;
    }
    appendParagraph(paragraphLines.join(" "));
  }

  return container;
}

async function renderSection(section) {
  const wrapper = document.createElement("div");
  wrapper.className = `section section-${section.slug}`;
  const variant = activeVariant(section);
  const profile = variant?.profile || section.profile;
  const markdownSrc = variant?.markdownSrc || section.markdownSrc;

  if (!section.hideHeader) {
    wrapper.appendChild(renderHeader(section));
  }

  if (profile) {
    wrapper.appendChild(renderProfile(profile));
  }

  if (Array.isArray(section.variants) && section.variants.length > 0) {
    wrapper.appendChild(renderVariantControls(section));
  }

  const documentActions = renderDocumentActions(section, variant);
  if (documentActions) {
    wrapper.appendChild(documentActions);
  }

  const inlineTarget = renderInlineTarget(section);
  if (inlineTarget) {
    wrapper.appendChild(inlineTarget);
  } else {
    wrapper.appendChild(renderBlocks(section.blocks));
  }

  if (markdownSrc) {
    const response = await fetch(markdownSrc, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`document request failed: ${response.status}`);
    }
    wrapper.appendChild(renderMarkdown(await response.text(), section.slug));
  }

  if (Array.isArray(section.mediaGroups)) {
    wrapper.appendChild(renderMediaGroups(section.mediaGroups));
  }

  if (Array.isArray(section.media)) {
    wrapper.appendChild(renderMediaStack(section.media));
  }

  content.replaceChildren(wrapper);
  content.focus({ preventScroll: true });
}

async function selectSection(slug, options = {}) {
  const route = resolveRoute(slug);
  const section = route.section;
  state.activeSlug = section.slug;
  if (route.inlineSlug) {
    state.activeInlineBySlug[section.slug] = route.inlineSlug;
  } else {
    delete state.activeInlineBySlug[section.slug];
  }

  const desiredHash = hashForRoute(section.slug, route.inlineSlug);
  if (options.updateHash && location.hash !== desiredHash) {
    history.pushState(null, "", desiredHash);
  } else if (route.replaceHash && location.hash !== desiredHash) {
    history.replaceState(null, "", desiredHash);
  }

  setActiveNav(section.slug);
  try {
    await renderSection(section);
    window.scrollTo({ top: 0, behavior: "auto" });
  } catch (error) {
    content.replaceChildren();
    const message = document.createElement("p");
    message.className = "error";
    message.textContent = "자료를 불러오지 못했습니다.";
    content.appendChild(message);
    console.error(error);
  }
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
