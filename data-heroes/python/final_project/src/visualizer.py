import os
import matplotlib.pyplot as plt

def save_dashboard(
        df_by_product,
        df_by_region,
        df_by_month,
        kpis: dict,
        n_top: int = 10,
        out_dir: str = "../reports/figures",
        filename: str = "dashboard.png"

):
    top = df_by_product.nlargest(n_top, "revenue").copy()
    fig, axs = plt.subplots(2, 2, figsize=(12,7))

    axs[0, 0].bar(top["product_name"], top["revenue"])
    axs[0, 0].set_title(f"Top {n_top} products by revenue")
    axs[0, 0].set_xlabel("Product")
    axs[0, 0].set_ylabel("Revenue")
    axs[0, 0].tick_params(axis="x", rotation=45)
    axs[0, 0].grid(axis="y", alpha=0.3)

    axs[0, 1].bar(df_by_region["region"], df_by_region["revenue"])
    axs[0, 1].set_title(f"Revenue by region")
    axs[0, 1].set_xlabel("Region")
    axs[0, 1].set_ylabel("Revenue")
    axs[0, 1].grid(axis="y", alpha=0.3)

    axs[1, 0].plot(df_by_month["year_month"], df_by_month["revenue"], marker="o")
    axs[1, 0].set_title(f"Revenue by month")
    axs[1, 0].set_xlabel("Month")
    axs[1, 0].set_ylabel("Revenue")
    axs[1, 0].tick_params(axis="x", rotation=45)
    axs[1, 0].grid(axis="y", alpha=0.3)

    axs[1, 1].axis("off")
    lines = [
        "KEY METRICS",
        "-------------",
        f"Total revenue: {kpis.get("total_revenue", 0):,.2f}",
        f"Total units: {kpis.get("total_units", 0):,.2f}",
        f"Avg price: {kpis.get("average_price", 0):,.2f}",
        f"Products: {kpis.get("distinct_products", 0)}",
        f"Customers: {kpis.get("distinct_customers", 0)}"
    ]
    text_block = "\n".join(lines)
    axs[1, 1].text(
        0.02, 0.98, text_block,
        va="top", ha="left",
        fontsize=11, family="Monospace"
    )

    fig.suptitle("Sales dashboard", fontsize=14, y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)

    out_path = os.path.join(out_dir, filename)

    plt.savefig(out_path, dpi=150)

    plt.close(fig)

    return out_path
