"""
Generate Web UI from GUI Model
This script demonstrates how to use the WebUIGenerator with a GUI model
"""

import os
import sys

from gui_model import GUIModel, Module, Screen
from besser_web_ui_generator import WebUIGenerator


def create_sample_gui_model():
    """Create the community platform GUI model"""
    gui = GUIModel(
        name="CommunityPlatform",
        package="com.example.community",
        versionCode="1",
        versionName="1.0",
        description="Community marketplace platform generated from DSML",
        screenCompatibility=True,
        modules=set()
    )

    # Create main module
    main_module = Module(name="MainModule", screens=set())
    gui.modules.add(main_module)

    # Create screens
    blank_screen = Screen(
        name="BlankScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(blank_screen)

    item_list_screen = Screen(
        name="ItemListScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=True
    )
    main_module.screens.add(item_list_screen)

    login_screen = Screen(
        name="LoginScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(login_screen)

    item_details_screen = Screen(
        name="ItemDetailsScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(item_details_screen)

    ratings_list_screen = Screen(
        name="RatingsListScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(ratings_list_screen)

    payment_screen = Screen(
        name="PaymentScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(payment_screen)

    return gui


def main():
    """Main generation function"""
    # Create the GUI model
    gui_model = create_sample_gui_model()

    # Create output directory
    output_dir = "./output_besser"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate web UI
    generator = WebUIGenerator(model=gui_model, output_dir=output_dir)
    generator.generate()

    print("\nWebsite ready at: " + output_dir)
    print("Open " + output_dir + "/index.html in your browser")


if __name__ == "__main__":
    main()
