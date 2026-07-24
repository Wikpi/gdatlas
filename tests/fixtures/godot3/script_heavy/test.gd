tool
extends Node2D
class_name Test

# Declare member variables here. Examples:
var a: int = 2
var is_true = true
const b: String = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

class TestClass:
	var c: float = 3.14

	func test() -> void:
		return

class TestNestedClass:
	var d: int = 1

	func test_init() -> bool:
		return true

	class RandomClass:
		var e: int = 2

		func test_init() -> bool:
			return false

		func _ready():
			return

enum TestEnum { TEST_MEMBER1, TEST_MEMBER2 }
