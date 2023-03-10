<script lang="ts">
  import "../app.postcss";
  import { page } from "$app/stores";
  import { DarkMode, Drawer, Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from "flowbite-svelte";
  import { Home, ChartBar, Cog, QuestionMarkCircle, Folder } from "svelte-heros-v2";

  $: activeUrl = $page.url.pathname;
  let activateClickOutside = false;
</script>

<Drawer
  backdrop={false}
  hidden={false}
  bind:activateClickOutside
  width="w-64"
  class="overflow-scroll pb-32"
  id="sidebar"
>
  <Sidebar asideClass="w-54">
    <SidebarWrapper divClass="overflow-y-auto py-4 px-3 rounded dark:bg-gray-800">
      <SidebarGroup>
        <SidebarItem label="LOGO" />
        <SidebarItem label="Home" href="/" active={activeUrl === `/`}>
          <svelte:fragment slot="icon">
            <Home />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Projects" href="/">
          <svelte:fragment slot="icon">
            <Folder />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Dashboard" href="/">
          <svelte:fragment slot="icon">
            <ChartBar />
          </svelte:fragment>
        </SidebarItem>
        <SidebarItem label="Setting" href="/">
          <svelte:fragment slot="icon">
            <Cog />
          </svelte:fragment>
        </SidebarItem>
        <DarkMode />
      </SidebarGroup>
      <SidebarGroup border>
        <SidebarItem label="Help" href="/">
          <svelte:fragment slot="icon">
            <QuestionMarkCircle />
          </svelte:fragment>
        </SidebarItem>
      </SidebarGroup>
    </SidebarWrapper>
  </Sidebar>
</Drawer>

<div class="flex px-4 mx-auto w-full">
  <main class="ml-64 w-full mx-auto">
    <slot />
  </main>
</div>
