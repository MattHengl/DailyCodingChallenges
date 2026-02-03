class _StoreManager:
    def __init__(self):
        self.store_list = []

    def add_store(self, store):
        self.store_list.append(store)

    def get_stores(self):
        return self.store_list

    def extend_stores(self, stores):
        self.store_list.extend(stores)

    def __getitem__(self, index):
        return self.store_list[index]

    @staticmethod
    def get_store(wanted_store_number):
        print(f"Checking for {wanted_store_number}")
        found_store = next((store for store in stores_list if store.store_number == wanted_store_number), False)
        print("Found the store in store list.") if found_store is not False else print("Could not find store in store list.")
        return found_store

    @staticmethod
    def display_stores():
        print("\nCurrent Locations:")
        for store in stores_list:
            print(f"- {store}")

stores_list = _StoreManager()

