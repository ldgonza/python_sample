from mamba import describe, it
from expects import expect, be

from python_sample.python_sample import my_sample

with describe(my_sample):
    with it("does"):
        result = my_sample("b")
        expect(result).to(be("b"))
