import pytest
from pathlib import Path
from PIL import Image
from app.main import shrink_image  

@pytest.fixture
def create_test_image(tmp_path):
    image_path = tmp_path / "test_image.png"
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save(image_path)
    return image_path

def test_shrink_image(create_test_image):
    input_image_path = create_test_image
    shrink_percentage = 50  # Shrink by 50%

    shrink_image(input_image_path, shrink_percentage)

    output_image_path = input_image_path.parent / f"{input_image_path.stem}.out{input_image_path.suffix}"
    with Image.open(output_image_path) as output_img:
        assert output_img.size == (50, 50), "Image size should be reduced to 50% of the original"

def test_shrink_image_invalid_path():
    with pytest.raises(FileNotFoundError):
        shrink_image("non_existent_image.png", 50)

def test_shrink_image_invalid_percentage(create_test_image):
    with pytest.raises(ValueError):
        shrink_image(create_test_image, 200)


