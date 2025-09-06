import reflex as rx

config = rx.Config(
    app_name="bvirtual.bvirtual",
    db_url="mysql+mysqldb://bvirtual:1234567.@localhost/bvirtual",
    api_url="http://localhost:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)