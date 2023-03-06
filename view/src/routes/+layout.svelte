<script lang="ts">
	import '../app.postcss';
	import { page } from '$app/stores';
	import { DarkMode, Drawer, Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';

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
				<SidebarItem label="home" href="/" active={activeUrl === `/`} />
				<DarkMode />
			</SidebarGroup>
		</SidebarWrapper>
	</Sidebar>
</Drawer>

<div class="flex px-4 mx-auto w-full">
	<main class="ml-64 w-full mx-auto">
		<slot />
	</main>
</div>
