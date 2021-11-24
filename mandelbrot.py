from PIL import Image

def mandelbrot(c: complex, z = 0, iterations = 100, bound = 10) -> complex:
    for _ in range(iterations):
        z = z ** 2 + c
        if (abs(z) > bound):
            break
    return z

canvas = 2056

print("Creating canvas")
image  = Image.new("RGB", (canvas, canvas), "white")
pixels = image.load()


print("Generating pixels")
for x in range(canvas):
    if not (x%(canvas/100)):
        print(f'{100*x / canvas}% done')
    for y in range(canvas):
        colour = mandelbrot(
            complex(
                x/(canvas/3) - 2,
                y/(canvas/3) - 1.5,
            ),
            0,
            100,
            10
        )
        pixels[x, y] = (20 * int(abs(colour.real)),
                        10 * int(abs(colour.imag)) % 100,
                        10 * int(abs(colour)) % 50)
print("Writing to image")
image.save(f'mandelbrot{canvas}.png')
print("Opening Image")
image.show()
