import Slider from "react-slick";

const ImageSlider = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
  };

  return (
    <div className="w-full max-w-2xl mx-auto mt-8">
      <Slider {...settings}>
        <div>
          <img 
            src="src\components\Slide1.png" 
            alt="Slide 1" 
            className="w-full h-80 object-cover rounded-xl" 
          />
        </div>
        <div>
          <img 
            src="src\components\Slide2.jpg" 
            alt="Slide 2" 
            className="w-full h-80 object-cover rounded-xl" 
          />
        </div>
        <div>
          <img 
            src="src\components\Slide3.jpg" 
            alt="Slide 3" 
            className="w-full h-80 object-cover rounded-xl"
          />
        </div>
      </Slider>
    </div>
  );
};

export default ImageSlider;
