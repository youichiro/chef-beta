<script lang="ts">
    import Annotation from "$lib/components/Annotation.svelte";
    import PageTop from "$lib/components/PageTop.svelte";

    type Category = {
        value: string;
        name: string;
        color: string;
    }
    const categories: Category[] = [
        { value: "名前", name: "名前", color: "yellow" },
        { value: "住所", name: "住所", color: "#98fb98" },
        { value: "電話番号", name: "電話番号", color: "orange" },
    ]
    const text = '私は小川耀一朗です';
    // const text = '私は小川耀一朗ですあああああああああああああ私は小川耀一朗ですあああああああああああああ私は小川耀一朗ですあああああああああああああ';
</script>

<PageTop title="Annotation" pages={["projects", "datasets", "tasks"]} />
<Annotation {categories} {text} />
