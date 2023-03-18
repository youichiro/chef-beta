<script lang="ts">
    import Annotation from "$lib/components/Annotation.svelte";
    import PageTop from "$lib/components/PageTop.svelte";

    type SelectItem = {
        value: string;
        name: string;
    }
    const categories: SelectItem[] = [
        { value: "名前", name: "名前" },
        { value: "住所", name: "住所" },
        { value: "電話番号", name: "電話番号" },
    ]
    const text = '私は小川耀一朗です';
</script>

<PageTop title="Annotation" pages={["projects", "datasets", "tasks"]} />
<Annotation {categories} {text} />
