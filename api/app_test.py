from app import process_query

def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled" + \
    "the Earth 200 million years ago"