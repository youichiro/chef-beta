<script lang="ts">
  import "../app.postcss";
  import { page } from "$app/stores";
  import { Drawer, Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from "flowbite-svelte";
  import { Home, ChartBar, Cog, QuestionMarkCircle, Folder } from "svelte-heros-v2";

  $: activeUrl = $page.url.pathname;
  let activateClickOutside = false;

  const styles = {
    sidebarItem: {
      base: "flex item-center p-4 text-gray-500 hover:bg-gray-100 hover:text-gray-700",
      active: "flex item-center py-4 px-3 text-black border-l-4 border-orange-500"
    },
    hoge: {
      aClass: "bg-red",
      activeClass: "bg-blue"
    }
  }
</script>

<Drawer
  id="sidebar"
  backdrop={false}
  hidden={false}
  bind:activateClickOutside
  divClass="verflow-y-auto z-50 bg-white"
  width="w-64"
  class="overflow-scroll border"
>
  <Sidebar>
    <SidebarWrapper divClass="overflow-y-auto py-4">
      <SidebarGroup ulClass="">
        <SidebarItem label="LOGO" />
        <SidebarItem label="Home" href="/" active={activeUrl === "/"} aClass={styles.sidebarItem.base} activeClass={styles.sidebarItem.active}>
          <svelte:fragment slot="icon">
            <Home />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Projects" href="/projects" active={activeUrl.startsWith("/projects")} aClass={styles.sidebarItem.base} activeClass={styles.sidebarItem.active}>
          <svelte:fragment slot="icon">
            <Folder />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Dashboard" href="/" aClass={styles.sidebarItem.base} activeClass={styles.sidebarItem.active}>
          <svelte:fragment slot="icon">
            <ChartBar />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Setting" href="/" aClass={styles.sidebarItem.base} activeClass={styles.sidebarItem.active}>
          <svelte:fragment slot="icon">
            <Cog />
          </svelte:fragment>
        </SidebarItem>
      </SidebarGroup>
      <SidebarGroup border ulClass="">
        <SidebarItem label="Help" href="/" aClass={styles.sidebarItem.base}>
          <svelte:fragment slot="icon">
            <QuestionMarkCircle />
          </svelte:fragment>
        </SidebarItem>
      </SidebarGroup>
    </SidebarWrapper>
  </Sidebar>
</Drawer>

<div class="flex mx-auto w-full dark:bg-gray-800">
  <main class="ml-64 w-full mx-auto">
    <slot />
  </main>
</div>
