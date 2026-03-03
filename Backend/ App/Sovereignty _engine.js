const stats = $input.item.json;

const MINT_THRESHOLD = 500000;

if (stats.views >= MINT_THRESHOLD || stats.likes >= MINT_THRESHOLD) {
    return {
        json: {
            action: "MINT_NFT",
            asset_type: stats.type,
            metadata: {
                creator: "Nia LeSane CEO",
                theory: "Quantum Music Frequency Alignment",
                owner_email: "lesane1972@gmail.com"
            },
            status: "Sovereign Asset Created"
        }
    };
} else {
    return { json: { status: "ACCUMULATING_CLOUT", current: stats.views } };
}
