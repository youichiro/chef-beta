<script>
    import Annotation from "$lib/components/Annotation.svelte";
    import PageTop from "$lib/components/PageTop.svelte";

    const categories = ['名前', '住所', '電話番号'];
    const text = '私は小川耀一朗です';
</script>

<PageTop title="Annotation" pages={["projects", "datasets", "tasks"]} />
<Annotation {categories} {text} />
