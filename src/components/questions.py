
import dash_bootstrap_components as dbc
from dash import html


def render() -> html.Section:
    return html.Section(
        dbc.Container(
            [
                html.H2(
                    "Frequently Asked Questions",
                    className="text-center mb-4"
                ),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam beatae fuga animi distinctio perspiciatis adipisci velit maiores totam tempora accusamus modi explicabo accusantium consequatur, praesentium rem quisquam molestias at quos vero. Officiis ad velit doloremque at. Dignissimos praesentium necessitatibus natus corrupti cum consequatur aliquam! Minima molestias iure quam distinctio velit.",
                            title="Where exactly are you located?"
                        ),
                        dbc.AccordionItem(
                            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam beatae fuga animi distinctio perspiciatis adipisci velit maiores totam tempora accusamus modi explicabo accusantium consequatur, praesentium rem quisquam molestias at quos vero. Officiis ad velit doloremque at. Dignissimos praesentium necessitatibus natus corrupti cum consequatur aliquam! Minima molestias iure quam distinctio velit.",
                            title="How much does it cost to attend?"
                        ),
                        dbc.AccordionItem(
                            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam beatae fuga animi distinctio perspiciatis adipisci velit maiores totam tempora accusamus modi explicabo accusantium consequatur, praesentium rem quisquam molestias at quos vero. Officiis ad velit doloremque at. Dignissimos praesentium necessitatibus natus corrupti cum consequatur aliquam! Minima molestias iure quam distinctio velit.",
                            title="What do I need to Know?"
                        ),
                        dbc.AccordionItem(
                            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam beatae fuga animi distinctio perspiciatis adipisci velit maiores totam tempora accusamus modi explicabo accusantium consequatur, praesentium rem quisquam molestias at quos vero. Officiis ad velit doloremque at. Dignissimos praesentium necessitatibus natus corrupti cum consequatur aliquam! Minima molestias iure quam distinctio velit.",
                            title="How Do I sign up?"
                        ),
                        dbc.AccordionItem(
                            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam beatae fuga animi distinctio perspiciatis adipisci velit maiores totam tempora accusamus modi explicabo accusantium consequatur, praesentium rem quisquam molestias at quos vero. Officiis ad velit doloremque at. Dignissimos praesentium necessitatibus natus corrupti cum consequatur aliquam! Minima molestias iure quam distinctio velit.",
                            title="Do you help me find a job?"
                        ),
                    ],
                    class_name="accordion-flush",
                )
            ]
        ),
        id="questions",
        className="p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
    )