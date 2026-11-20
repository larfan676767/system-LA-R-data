import sys
import json
import copy
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox,
                             QTableWidget, QTableWidgetItem, QTabWidget, QMessageBox, QFileDialog,
                             QScrollArea, QGroupBox, QCheckBox, QListWidget, QListWidgetItem,
                             QSplitter, QFrame, QDialog, QDialogButtonBox, QDoubleSpinBox)
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QFont, QPalette, QColor, QIcon, QPainter, QLinearGradient


class XeraTheme:
    PRIMARY = "#2d2d30"
    SECONDARY = "#3e3e42"
    BACKGROUND = "#1e1e1e"
    SURFACE = "#252526"
    SURFACE_LIGHT = "#2d2d30"
    TEXT = "#cccccc"
    TEXT_DIM = "#858585"
    ACCENT = "#007acc"
    ACCENT_HOVER = "#1c97ea"
    SUCCESS = "#4ec9b0"
    WARNING = "#ce9178"
    BORDER = "#3e3e42"
    
    @staticmethod
    def get_stylesheet():
        return f"""
            QMainWindow {{
                background-color: {XeraTheme.BACKGROUND};
            }}
            
            QWidget {{
                background-color: transparent;
                color: {XeraTheme.TEXT};
                font-family: 'Segoe UI', 'Arial', sans-serif;
                font-size: 10pt;
            }}
            
            QPushButton {{
                background-color: {XeraTheme.ACCENT};
                color: #ffffff;
                border: none;
                border-radius: 3px;
                padding: 8px 16px;
                font-weight: 500;
                font-size: 9pt;
            }}
            
            QPushButton:hover {{
                background-color: {XeraTheme.ACCENT_HOVER};
            }}
            
            QPushButton:pressed {{
                background-color: #005a9e;
            }}
            
            QPushButton:disabled {{
                background-color: {XeraTheme.SURFACE};
                color: {XeraTheme.TEXT_DIM};
            }}
            
            QPushButton.secondary {{
                background-color: {XeraTheme.SURFACE_LIGHT};
                color: {XeraTheme.TEXT};
                border: 1px solid {XeraTheme.BORDER};
            }}
            
            QPushButton.secondary:hover {{
                background-color: {XeraTheme.SECONDARY};
                border-color: {XeraTheme.ACCENT};
            }}
            
            QPushButton.danger {{
                background-color: #c5303a;
                color: white;
            }}
            
            QPushButton.danger:hover {{
                background-color: #d84850;
            }}
            
            QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {{
                background-color: {XeraTheme.SURFACE};
                color: {XeraTheme.TEXT};
                border: 1px solid {XeraTheme.BORDER};
                border-radius: 2px;
                padding: 6px;
                selection-background-color: {XeraTheme.ACCENT};
                selection-color: #ffffff;
            }}
            
            QLineEdit:focus, QTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {{
                border-color: {XeraTheme.ACCENT};
            }}
            
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            
            QComboBox::down-arrow {{
                image: none;
                border: 1px solid {XeraTheme.TEXT};
                width: 6px;
                height: 6px;
                border-top: none;
                border-left: none;
            }}
            
            QComboBox QAbstractItemView {{
                background-color: {XeraTheme.SURFACE};
                color: {XeraTheme.TEXT};
                selection-background-color: {XeraTheme.ACCENT};
                selection-color: #ffffff;
                border: 1px solid {XeraTheme.BORDER};
            }}
            
            QTableWidget {{
                background-color: {XeraTheme.SURFACE};
                alternate-background-color: {XeraTheme.SURFACE_LIGHT};
                gridline-color: {XeraTheme.BORDER};
                border: 1px solid {XeraTheme.BORDER};
            }}
            
            QTableWidget::item {{
                padding: 6px;
                color: {XeraTheme.TEXT};
            }}
            
            QTableWidget::item:selected {{
                background-color: {XeraTheme.ACCENT};
                color: #ffffff;
            }}
            
            QHeaderView::section {{
                background-color: {XeraTheme.PRIMARY};
                color: {XeraTheme.TEXT};
                padding: 8px;
                border: none;
                border-bottom: 1px solid {XeraTheme.BORDER};
                border-right: 1px solid {XeraTheme.BORDER};
                font-weight: 600;
            }}
            
            QTabWidget::pane {{
                border: 1px solid {XeraTheme.BORDER};
                background-color: {XeraTheme.SURFACE};
            }}
            
            QTabBar::tab {{
                background-color: {XeraTheme.SURFACE};
                color: {XeraTheme.TEXT_DIM};
                padding: 10px 20px;
                margin: 0px;
                border: 1px solid {XeraTheme.BORDER};
                border-bottom: none;
            }}
            
            QTabBar::tab:selected {{
                background-color: {XeraTheme.PRIMARY};
                color: {XeraTheme.TEXT};
                border-bottom: 2px solid {XeraTheme.ACCENT};
            }}
            
            QTabBar::tab:hover:!selected {{
                background-color: {XeraTheme.SURFACE_LIGHT};
                color: {XeraTheme.TEXT};
            }}
            
            QGroupBox {{
                border: 1px solid {XeraTheme.BORDER};
                border-radius: 2px;
                margin-top: 12px;
                padding-top: 16px;
                font-weight: 600;
            }}
            
            QGroupBox::title {{
                color: {XeraTheme.TEXT};
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }}
            
            QScrollBar:vertical {{
                background: {XeraTheme.SURFACE};
                width: 12px;
                border: none;
            }}
            
            QScrollBar::handle:vertical {{
                background: {XeraTheme.BORDER};
                min-height: 30px;
            }}
            
            QScrollBar::handle:vertical:hover {{
                background: {XeraTheme.TEXT_DIM};
            }}
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            
            QScrollBar:horizontal {{
                background: {XeraTheme.SURFACE};
                height: 12px;
                border: none;
            }}
            
            QScrollBar::handle:horizontal {{
                background: {XeraTheme.BORDER};
                min-width: 30px;
            }}
            
            QScrollBar::handle:horizontal:hover {{
                background: {XeraTheme.TEXT_DIM};
            }}
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
                width: 0px;
            }}
            
            QListWidget {{
                background-color: {XeraTheme.SURFACE};
                border: 1px solid {XeraTheme.BORDER};
            }}
            
            QListWidget::item {{
                padding: 8px;
                border-bottom: 1px solid {XeraTheme.BORDER};
            }}
            
            QListWidget::item:selected {{
                background-color: {XeraTheme.ACCENT};
                color: #ffffff;
            }}
            
            QListWidget::item:hover {{
                background-color: {XeraTheme.SURFACE_LIGHT};
            }}
            
            QCheckBox {{
                spacing: 6px;
            }}
            
            QCheckBox::indicator {{
                width: 16px;
                height: 16px;
                border: 1px solid {XeraTheme.BORDER};
                background: {XeraTheme.SURFACE};
            }}
            
            QCheckBox::indicator:checked {{
                background: {XeraTheme.ACCENT};
                border-color: {XeraTheme.ACCENT};
            }}
            
            QLabel {{
                color: {XeraTheme.TEXT};
            }}
            
            QLabel.header {{
                color: {XeraTheme.TEXT};
                font-size: 13pt;
                font-weight: 600;
            }}
            
            QLabel.subheader {{
                color: {XeraTheme.TEXT_DIM};
                font-size: 9pt;
            }}
            
            QMessageBox {{
                background-color: {XeraTheme.SURFACE};
            }}
            
            QSplitter::handle {{
                background-color: {XeraTheme.BORDER};
            }}
            
            QSplitter::handle:horizontal {{
                width: 2px;
            }}
            
            QSplitter::handle:vertical {{
                height: 2px;
            }}
            
            QDialog {{
                background-color: {XeraTheme.BACKGROUND};
            }}
        """


class ItemEditorDialog(QDialog):
    def __init__(self, parent=None, item_data=None, is_new=False):
        super().__init__(parent)
        self.item_data = item_data if item_data else {}
        self.is_new = is_new
        
        self.setWindowTitle("XERA GAMES - Edit Item" if not is_new else "XERA GAMES - New Item")
        self.setMinimumSize(800, 700)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        title = QLabel("ITEM CONFIGURATION" if self.is_new else "ITEM EDITOR")
        title.setProperty("class", "header")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        form_layout = QVBoxLayout()
        
        basic_group = QGroupBox("Basic Information")
        basic_layout = QVBoxLayout()
        
        self.item_id_input = self.create_field("Item ID:", self.item_data.get("ItemId", ""))
        self.display_name_input = self.create_field("Display Name:", self.item_data.get("DisplayName", ""))
        self.description_input = self.create_text_field("Description:", self.item_data.get("Description", ""))
        
        basic_layout.addLayout(self.create_field_layout("Item ID:", self.item_id_input))
        basic_layout.addLayout(self.create_field_layout("Display Name:", self.display_name_input))
        basic_layout.addLayout(self.create_field_layout("Description:", self.description_input))
        
        self.item_class_input = QComboBox()
        self.item_class_input.addItems(["", "HEAD", "BODY", "FACE", "HAND", "EYE", "NAMETAG", "SKIN", 
                                        "MONSTER", "MonsterSkin", "PLAYERMODEL", "HOODLUM_NIGGA", "SantaBundle"])
        self.item_class_input.setEditable(True)
        self.item_class_input.setCurrentText(self.item_data.get("ItemClass", "") or "")
        basic_layout.addLayout(self.create_field_layout("Item Class:", self.item_class_input))
        
        basic_group.setLayout(basic_layout)
        form_layout.addWidget(basic_group)
        
        currency_group = QGroupBox("Virtual Currency Prices")
        currency_layout = QVBoxLayout()
        
        self.currency_table = QTableWidget()
        self.currency_table.setColumnCount(2)
        self.currency_table.setHorizontalHeaderLabels(["Currency Code", "Price"])
        self.currency_table.horizontalHeader().setStretchLastSection(True)
        
        virtual_prices = self.item_data.get("VirtualCurrencyPrices", {})
        if virtual_prices:
            self.currency_table.setRowCount(len(virtual_prices))
            for i, (code, price) in enumerate(virtual_prices.items()):
                self.currency_table.setItem(i, 0, QTableWidgetItem(code))
                self.currency_table.setItem(i, 1, QTableWidgetItem(str(price)))
        
        currency_layout.addWidget(self.currency_table)
        
        currency_btn_layout = QHBoxLayout()
        add_currency_btn = QPushButton("Add Currency")
        add_currency_btn.clicked.connect(self.add_currency_row)
        remove_currency_btn = QPushButton("Remove Selected")
        remove_currency_btn.setProperty("class", "danger")
        remove_currency_btn.clicked.connect(self.remove_currency_row)
        currency_btn_layout.addWidget(add_currency_btn)
        currency_btn_layout.addWidget(remove_currency_btn)
        currency_layout.addLayout(currency_btn_layout)
        
        currency_group.setLayout(currency_layout)
        form_layout.addWidget(currency_group)
        
        flags_group = QGroupBox("Item Flags")
        flags_layout = QVBoxLayout()
        
        self.is_stackable = QCheckBox("Is Stackable")
        self.is_stackable.setChecked(self.item_data.get("IsStackable", False))
        self.is_tradable = QCheckBox("Is Tradable")
        self.is_tradable.setChecked(self.item_data.get("IsTradable", False))
        self.is_limited = QCheckBox("Is Limited Edition")
        self.is_limited.setChecked(self.item_data.get("IsLimitedEdition", False))
        
        flags_layout.addWidget(self.is_stackable)
        flags_layout.addWidget(self.is_tradable)
        flags_layout.addWidget(self.is_limited)
        
        flags_group.setLayout(flags_layout)
        form_layout.addWidget(flags_group)
        
        bundle_group = QGroupBox("Bundle Configuration")
        bundle_layout = QVBoxLayout()
        
        self.is_bundle = QCheckBox("This is a Bundle")
        self.is_bundle.setChecked(self.item_data.get("Bundle") is not None)
        self.is_bundle.stateChanged.connect(self.toggle_bundle_fields)
        bundle_layout.addWidget(self.is_bundle)
        
        self.bundle_items_list = QListWidget()
        self.bundle_items_list.setMaximumHeight(150)
        bundle_data = self.item_data.get("Bundle", {})
        if bundle_data and "BundledItems" in bundle_data:
            for item in bundle_data["BundledItems"]:
                self.bundle_items_list.addItem(item)
        
        bundle_layout.addWidget(QLabel("Bundled Items:"))
        bundle_layout.addWidget(self.bundle_items_list)
        
        bundle_btn_layout = QHBoxLayout()
        self.add_bundle_item_btn = QPushButton("Add Item ID")
        self.add_bundle_item_btn.clicked.connect(self.add_bundle_item)
        self.remove_bundle_item_btn = QPushButton("Remove Selected")
        self.remove_bundle_item_btn.setProperty("class", "danger")
        self.remove_bundle_item_btn.clicked.connect(self.remove_bundle_item)
        bundle_btn_layout.addWidget(self.add_bundle_item_btn)
        bundle_btn_layout.addWidget(self.remove_bundle_item_btn)
        bundle_layout.addLayout(bundle_btn_layout)
        
        self.bundle_currency_table = QTableWidget()
        self.bundle_currency_table.setColumnCount(2)
        self.bundle_currency_table.setHorizontalHeaderLabels(["Currency Code", "Amount"])
        self.bundle_currency_table.setMaximumHeight(120)
        
        if bundle_data and "BundledVirtualCurrencies" in bundle_data and bundle_data["BundledVirtualCurrencies"]:
            currencies = bundle_data["BundledVirtualCurrencies"]
            self.bundle_currency_table.setRowCount(len(currencies))
            for i, (code, amount) in enumerate(currencies.items()):
                self.bundle_currency_table.setItem(i, 0, QTableWidgetItem(code))
                self.bundle_currency_table.setItem(i, 1, QTableWidgetItem(str(amount)))
        
        bundle_layout.addWidget(QLabel("Bundled Currencies:"))
        bundle_layout.addWidget(self.bundle_currency_table)
        
        bundle_currency_btn_layout = QHBoxLayout()
        self.add_bundle_currency_btn = QPushButton("Add Currency")
        self.add_bundle_currency_btn.clicked.connect(self.add_bundle_currency_row)
        self.remove_bundle_currency_btn = QPushButton("Remove Selected")
        self.remove_bundle_currency_btn.setProperty("class", "danger")
        self.remove_bundle_currency_btn.clicked.connect(self.remove_bundle_currency_row)
        bundle_currency_btn_layout.addWidget(self.add_bundle_currency_btn)
        bundle_currency_btn_layout.addWidget(self.remove_bundle_currency_btn)
        bundle_layout.addLayout(bundle_currency_btn_layout)
        
        bundle_group.setLayout(bundle_layout)
        form_layout.addWidget(bundle_group)
        
        self.toggle_bundle_fields()
        
        scroll_content.setLayout(form_layout)
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
    
    def create_field(self, label_text, default_value):
        field = QLineEdit()
        field.setText(str(default_value))
        return field
    
    def create_text_field(self, label_text, default_value):
        field = QTextEdit()
        field.setPlainText(str(default_value) if default_value else "")
        field.setMaximumHeight(80)
        return field
    
    def create_field_layout(self, label_text, widget):
        layout = QVBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)
        layout.addWidget(widget)
        return layout
    
    def toggle_bundle_fields(self):
        is_bundle = self.is_bundle.isChecked()
        self.bundle_items_list.setEnabled(is_bundle)
        self.add_bundle_item_btn.setEnabled(is_bundle)
        self.remove_bundle_item_btn.setEnabled(is_bundle)
        self.bundle_currency_table.setEnabled(is_bundle)
        self.add_bundle_currency_btn.setEnabled(is_bundle)
        self.remove_bundle_currency_btn.setEnabled(is_bundle)
    
    def add_currency_row(self):
        row = self.currency_table.rowCount()
        self.currency_table.insertRow(row)
        self.currency_table.setItem(row, 0, QTableWidgetItem("GD"))
        self.currency_table.setItem(row, 1, QTableWidgetItem("0"))
    
    def remove_currency_row(self):
        current_row = self.currency_table.currentRow()
        if current_row >= 0:
            self.currency_table.removeRow(current_row)
    
    def add_bundle_item(self):
        text, ok = QLineEdit().text(), True
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Bundle Item")
        layout = QVBoxLayout()
        label = QLabel("Enter Item ID:")
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = input_field.text()
            if text:
                self.bundle_items_list.addItem(text)
    
    def remove_bundle_item(self):
        current_row = self.bundle_items_list.currentRow()
        if current_row >= 0:
            self.bundle_items_list.takeItem(current_row)
    
    def add_bundle_currency_row(self):
        row = self.bundle_currency_table.rowCount()
        self.bundle_currency_table.insertRow(row)
        self.bundle_currency_table.setItem(row, 0, QTableWidgetItem("GD"))
        self.bundle_currency_table.setItem(row, 1, QTableWidgetItem("0"))
    
    def remove_bundle_currency_row(self):
        current_row = self.bundle_currency_table.currentRow()
        if current_row >= 0:
            self.bundle_currency_table.removeRow(current_row)
    
    def get_item_data(self):
        virtual_prices = {}
        for row in range(self.currency_table.rowCount()):
            code_item = self.currency_table.item(row, 0)
            price_item = self.currency_table.item(row, 1)
            if code_item and price_item:
                try:
                    virtual_prices[code_item.text()] = int(price_item.text())
                except ValueError:
                    virtual_prices[code_item.text()] = 0
        
        bundle_data = None
        if self.is_bundle.isChecked():
            bundled_items = []
            for i in range(self.bundle_items_list.count()):
                bundled_items.append(self.bundle_items_list.item(i).text())
            
            bundled_currencies = None
            if self.bundle_currency_table.rowCount() > 0:
                bundled_currencies = {}
                for row in range(self.bundle_currency_table.rowCount()):
                    code_item = self.bundle_currency_table.item(row, 0)
                    amount_item = self.bundle_currency_table.item(row, 1)
                    if code_item and amount_item:
                        try:
                            bundled_currencies[code_item.text()] = int(amount_item.text())
                        except ValueError:
                            bundled_currencies[code_item.text()] = 0
            
            bundle_data = {
                "BundledItems": bundled_items,
                "BundledResultTables": [],
                "BundledVirtualCurrencies": bundled_currencies
            }
        
        item_class = self.item_class_input.currentText()
        if not item_class:
            item_class = None
        
        return {
            "ItemId": self.item_id_input.text(),
            "ItemClass": item_class,
            "CatalogVersion": "Main",
            "DisplayName": self.display_name_input.text() or None,
            "Description": self.description_input.toPlainText() or None,
            "VirtualCurrencyPrices": virtual_prices,
            "RealCurrencyPrices": {} if not virtual_prices else {},
            "Tags": [],
            "CustomData": None,
            "Consumable": {
                "UsageCount": None,
                "UsagePeriod": None,
                "UsagePeriodGroup": None
            },
            "Container": None,
            "Bundle": bundle_data,
            "CanBecomeCharacter": False,
            "IsStackable": self.is_stackable.isChecked(),
            "IsTradable": self.is_tradable.isChecked(),
            "ItemImageUrl": None,
            "IsLimitedEdition": self.is_limited.isChecked(),
            "InitialLimitedEditionCount": 0,
            "ActivatedMembership": None
        }


class LocalAvaiteCatalogEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.catalog_data = None
        self.current_file_path = None
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("XERA GAMES - LocalAvaite Catalog Editor")
        self.setMinimumSize(1400, 900)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        header = self.create_header()
        main_layout.addWidget(header)
        
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(15)
        
        toolbar_layout = QHBoxLayout()
        
        self.open_btn = QPushButton("Open Catalog")
        self.open_btn.clicked.connect(self.open_catalog)
        
        self.save_btn = QPushButton("Save As")
        self.save_btn.clicked.connect(self.save_catalog)
        self.save_btn.setEnabled(False)
        
        self.overwrite_btn = QPushButton("Overwrite")
        self.overwrite_btn.clicked.connect(self.overwrite_catalog)
        self.overwrite_btn.setEnabled(False)
        
        self.new_item_btn = QPushButton("New Item")
        self.new_item_btn.clicked.connect(self.create_new_item)
        self.new_item_btn.setEnabled(False)
        
        self.stats_label = QLabel("No catalog loaded")
        self.stats_label.setProperty("class", "subheader")
        
        toolbar_layout.addWidget(self.open_btn)
        toolbar_layout.addWidget(self.save_btn)
        toolbar_layout.addWidget(self.overwrite_btn)
        toolbar_layout.addWidget(self.new_item_btn)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.stats_label)
        
        content_layout.addLayout(toolbar_layout)
        
        self.tabs = QTabWidget()
        
        self.items_tab = self.create_items_tab()
        self.raw_tab = self.create_raw_tab()
        
        self.tabs.addTab(self.items_tab, "Items")
        self.tabs.addTab(self.raw_tab, "Raw JSON")
        
        content_layout.addWidget(self.tabs)
        
        main_layout.addLayout(content_layout)
        
        footer = self.create_footer()
        main_layout.addWidget(footer)
        
        central_widget.setLayout(main_layout)
    
    def create_header(self):
        header = QFrame()
        header.setFixedHeight(80)
        header.setStyleSheet(f"""
            QFrame {{
                background-color: {XeraTheme.PRIMARY};
                border: none;
                border-bottom: 2px solid {XeraTheme.ACCENT};
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 10, 30, 10)
        
        title = QLabel("XERA GAMES")
        title.setStyleSheet(f"color: {XeraTheme.TEXT}; font-size: 20pt; font-weight: 600;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("LocalAvaite Catalog Editor v2.0")
        subtitle.setStyleSheet(f"color: {XeraTheme.TEXT_DIM}; font-size: 11pt;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title)
        layout.addWidget(subtitle)
        
        header.setLayout(layout)
        return header
    
    def create_footer(self):
        footer = QFrame()
        footer.setFixedHeight(40)
        footer.setStyleSheet(f"""
            QFrame {{
                background-color: {XeraTheme.PRIMARY};
                border-top: 1px solid {XeraTheme.BORDER};
            }}
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 0, 20, 0)
        
        copyright_label = QLabel("SOFTWARE BY XERA GAMES LLC | THIS SOFTWARE IS PROPRIETARY | DO NOT DISTRIBUTE")
        copyright_label.setStyleSheet(f"color: {XeraTheme.TEXT_DIM}; font-size: 8pt;")
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(copyright_label)
        
        footer.setLayout(layout)
        return footer
    
    def create_items_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Filter by Item ID, Display Name, or Class...")
        self.search_input.textChanged.connect(self.filter_items)
        
        self.class_filter = QComboBox()
        self.class_filter.addItem("All Classes")
        self.class_filter.currentTextChanged.connect(self.filter_items)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input, 3)
        search_layout.addWidget(QLabel("Class:"))
        search_layout.addWidget(self.class_filter, 1)
        
        layout.addLayout(search_layout)
        
        self.items_table = QTableWidget()
        self.items_table.setColumnCount(6)
        self.items_table.setHorizontalHeaderLabels(["Item ID", "Display Name", "Class", "Prices", "Bundle", "Actions"])
        self.items_table.horizontalHeader().setStretchLastSection(True)
        self.items_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.items_table.setAlternatingRowColors(True)
        
        layout.addWidget(self.items_table)
        
        widget.setLayout(layout)
        return widget
    
    def create_raw_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("Raw JSON Editor - Advanced users only")
        label.setProperty("class", "subheader")
        layout.addWidget(label)
        
        self.raw_editor = QTextEdit()
        self.raw_editor.setFont(QFont("Consolas", 10))
        layout.addWidget(self.raw_editor)
        
        btn_layout = QHBoxLayout()
        
        validate_btn = QPushButton("Validate JSON")
        validate_btn.clicked.connect(self.validate_json)
        
        apply_btn = QPushButton("Apply Changes")
        apply_btn.clicked.connect(self.apply_raw_changes)
        
        btn_layout.addWidget(validate_btn)
        btn_layout.addWidget(apply_btn)
        btn_layout.addStretch()
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        return widget
    
    def open_catalog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open LocalAvaite Catalog",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.catalog_data = json.load(f)
                
                self.current_file_path = file_path
                self.load_catalog()
                self.save_btn.setEnabled(True)
                self.overwrite_btn.setEnabled(True)
                self.new_item_btn.setEnabled(True)
                
                QMessageBox.information(self, "Success", f"Catalog loaded successfully!\n\n{len(self.catalog_data.get('Catalog', []))} items found.")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load catalog:\n{str(e)}")
    
    def load_catalog(self):
        if not self.catalog_data:
            return
        
        items = self.catalog_data.get("Catalog", [])
        
        self.stats_label.setText(f"{len(items)} items loaded | Version: {self.catalog_data.get('CatalogVersion', 'Unknown')}")
        
        self.items_table.setRowCount(0)
        
        classes = set()
        for item in items:
            item_class = item.get("ItemClass")
            if item_class:
                classes.add(item_class)
        
        self.class_filter.clear()
        self.class_filter.addItem("All Classes")
        self.class_filter.addItems(sorted(classes))
        
        self.populate_items_table(items)
        
        self.raw_editor.setPlainText(json.dumps(self.catalog_data, indent=2))
    
    def populate_items_table(self, items):
        self.items_table.setRowCount(len(items))
        
        for row, item in enumerate(items):
            self.items_table.setItem(row, 0, QTableWidgetItem(item.get("ItemId", "")))
            self.items_table.setItem(row, 1, QTableWidgetItem(item.get("DisplayName", "") or ""))
            self.items_table.setItem(row, 2, QTableWidgetItem(item.get("ItemClass", "") or ""))
            
            prices = item.get("VirtualCurrencyPrices", {})
            price_str = ", ".join([f"{k}: {v}" for k, v in prices.items()]) if prices else "Free"
            self.items_table.setItem(row, 3, QTableWidgetItem(price_str))
            
            is_bundle = "Yes" if item.get("Bundle") else "No"
            self.items_table.setItem(row, 4, QTableWidgetItem(is_bundle))
            
            actions_widget = QWidget()
            actions_layout = QHBoxLayout()
            actions_layout.setContentsMargins(5, 2, 5, 2)
            actions_layout.setSpacing(5)
            
            edit_btn = QPushButton("Edit")
            edit_btn.setMaximumWidth(70)
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_item(r))
            
            delete_btn = QPushButton("Delete")
            delete_btn.setProperty("class", "danger")
            delete_btn.setMaximumWidth(70)
            delete_btn.clicked.connect(lambda checked, r=row: self.delete_item(r))
            
            actions_layout.addWidget(edit_btn)
            actions_layout.addWidget(delete_btn)
            actions_layout.addStretch()
            actions_widget.setLayout(actions_layout)
            
            self.items_table.setCellWidget(row, 5, actions_widget)
        
        self.items_table.resizeColumnsToContents()
    
    def filter_items(self):
        if not self.catalog_data:
            return
        
        search_text = self.search_input.text().lower()
        class_filter = self.class_filter.currentText()
        
        items = self.catalog_data.get("Catalog", [])
        filtered_items = []
        
        for item in items:
            if class_filter != "All Classes" and item.get("ItemClass") != class_filter:
                continue
            
            if search_text:
                item_id = item.get("ItemId", "").lower()
                display_name = (item.get("DisplayName") or "").lower()
                item_class = (item.get("ItemClass") or "").lower()
                
                if search_text not in item_id and search_text not in display_name and search_text not in item_class:
                    continue
            
            filtered_items.append(item)
        
        self.populate_items_table(filtered_items)
    
    def create_new_item(self):
        dialog = ItemEditorDialog(self, is_new=True)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_item = dialog.get_item_data()
            
            if not new_item["ItemId"]:
                QMessageBox.warning(self, "Warning", "Item ID cannot be empty!")
                return
            
            existing_ids = [item["ItemId"] for item in self.catalog_data.get("Catalog", [])]
            if new_item["ItemId"] in existing_ids:
                QMessageBox.warning(self, "Warning", "Item ID already exists!")
                return
            
            self.catalog_data["Catalog"].append(new_item)
            self.load_catalog()
            QMessageBox.information(self, "Success", "Item created successfully!")
    
    def edit_item(self, row):
        item_id = self.items_table.item(row, 0).text()
        
        items = self.catalog_data.get("Catalog", [])
        item_index = None
        for i, item in enumerate(items):
            if item["ItemId"] == item_id:
                item_index = i
                break
        
        if item_index is None:
            return
        
        dialog = ItemEditorDialog(self, item_data=items[item_index])
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_item = dialog.get_item_data()
            self.catalog_data["Catalog"][item_index] = updated_item
            self.load_catalog()
            QMessageBox.information(self, "Success", "Item updated successfully!")
    
    def delete_item(self, row):
        item_id = self.items_table.item(row, 0).text()
        
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete item '{item_id}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            items = self.catalog_data.get("Catalog", [])
            self.catalog_data["Catalog"] = [item for item in items if item["ItemId"] != item_id]
            self.load_catalog()
            QMessageBox.information(self, "Success", "Item deleted successfully!")
    
    def save_catalog(self):
        if not self.catalog_data:
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save LocalAvaite Catalog",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.catalog_data, f, indent=2)
                
                QMessageBox.information(self, "Success", "Catalog saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save catalog:\n{str(e)}")
    
    def overwrite_catalog(self):
        if not self.catalog_data or not self.current_file_path:
            return
        
        reply = QMessageBox.question(
            self,
            "Confirm Overwrite",
            f"Are you sure you want to overwrite the original file?\n\n{self.current_file_path}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                with open(self.current_file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.catalog_data, f, indent=2)
                
                QMessageBox.information(self, "Success", "Catalog overwritten successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to overwrite catalog:\n{str(e)}")
    
    def validate_json(self):
        try:
            json.loads(self.raw_editor.toPlainText())
            QMessageBox.information(self, "Valid", "JSON is valid!")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Invalid JSON", f"JSON validation failed:\n{str(e)}")
    
    def apply_raw_changes(self):
        try:
            new_data = json.loads(self.raw_editor.toPlainText())
            
            reply = QMessageBox.question(
                self,
                "Confirm Changes",
                "Are you sure you want to apply these raw JSON changes?\nThis will replace the current catalog data.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.catalog_data = new_data
                self.load_catalog()
                QMessageBox.information(self, "Success", "Raw changes applied successfully!")
                
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Invalid JSON", f"Cannot apply changes. JSON is invalid:\n{str(e)}")


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(XeraTheme.get_stylesheet())
    
    editor = LocalAvaiteCatalogEditor()
    editor.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()