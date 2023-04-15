<script lang="ts">
  import "../app.postcss";
  import { page } from "$app/stores";
  import { Drawer, Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from "flowbite-svelte";
  import { Home, ChartBar, Cog, QuestionMarkCircle, Folder, Users } from "svelte-heros-v2";
  import type { SvelteComponent } from "svelte";

  $: activeUrl = $page.url.pathname;
  let activateClickOutside = false;

  type Item = {
    label: string;
    url: string,
    icon: typeof SvelteComponent;
  }

  const items: Item[] = [
    { label: "Home", url: "/", icon: Home },
    { label: "Projects", url: "/projects", icon: Folder },
    { label: "Members", url: "/members", icon: Users },
    { label: "Dashboard", url: "/", icon: ChartBar },
    { label: "Setting", url: "/", icon: Cog },
  ]

  const styles = {
    sidebarItem: {
      base: "flex item-center py-3 px-4 text-gray-500 hover:bg-gray-50 hover:text-gray-700",
      active: "flex item-center py-3 px-3 text-black border-l-4 border-orange-500",
    },
  };
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
        {#each items as item}
          <SidebarItem
            label={item.label}
            href={item.url}
            active={activeUrl === item.url}
            aClass={styles.sidebarItem.base}
            activeClass={styles.sidebarItem.active}
          >
            <svelte:fragment slot="icon">
              <svelte:component this={item.icon} />
            </svelte:fragment>
          </SidebarItem>
        {/each}
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
