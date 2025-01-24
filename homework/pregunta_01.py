# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os


def pregunta_01():
    def load_data():
        df = pd.read_csv("files/input/shipping-data.csv")
        return df
    output_dir = os.path.join(os.path.dirname(__file__), "../docs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    def create_visual_for_shipping_per_warehouse(df):
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(os.path.join(output_dir, "shipping_per_warehouse.png"))

    def create_visual_for_mode_of_shipment(df):
        df = df.copy()
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.savefig(os.path.join(output_dir, "mode_of_shipment.png"))

    def create_visual_for_average_customer_rating(df):
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df = df[["mean", "min", "max"]]
        plt.barh(
            y=df.index.values,
            width=df["max"].values - 1,
            left=df["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors = [
            "tab:green" if value >= 3.0 else "tab:orange"
            for value in df["mean"].values
        ]
        plt.barh(
            y=df.index.values,
            width=df["mean"].values - 1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_visible(True)
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(os.path.join(output_dir, "average_customer_rating.png"))

    def create_visual_for_weight_distribution(df):
        df = df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(os.path.join(output_dir, "weight_distribution.png"))
    df = load_data()
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)
    ruta_html = os.path.join(output_dir, "index.html")
    contenido_html = f"""
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Shipping Dashboard Example</h1>
            <div style="width:45%;float:left">
                <img src="shipping_per_warehouse.png" alt="Fig 1">
                <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%;float:left">
                <img src="average_customer_rating.png" alt="Fig 3">
                <img src="weight_distribution.png" alt="Fig 4">
            </div>
        </body>
    </html>
    """
    with open(ruta_html, "w") as file:
        file.write(contenido_html)

if __name__ == "__main__":
    pregunta_01()
"""
El archivo `files//shipping-data.csv` contiene información sobre los envios
de productos de una empresa. Cree un dashboard estático en HTML que
permita visualizar los siguientes campos:

* `Warehouse_block`

* `Mode_of_Shipment`

* `Customer_rating`

* `Weight_in_gms`

El dashboard generado debe ser similar a este:

https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

Para ello, siga las instrucciones dadas en el siguiente video:

https://youtu.be/AgbWALiAGVo

Tenga en cuenta los siguientes cambios respecto al video:

* El archivo de datos se encuentra en la carpeta `data`.

* Todos los archivos debe ser creados en la carpeta `docs`.

* Su código debe crear la carpeta `docs` si no existe.

"""
