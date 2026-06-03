import base64

from django.core.files.base import ContentFile

from pokedex.models import Pokemon, Trainer
from rest_framework import serializers


class PokemonSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(read_only=True)
    picture = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Pokemon
        fields = "__all__"

    def _decode_base64_image(self, value):
        if value:
            try:
                format_info, imgstr = value.split(";base64,")
                ext = format_info.split("/")[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f"pokemon.{ext}",
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 valida.")
        return value

    def validate_picture(self, value):
        return self._decode_base64_image(value)

    def validate(self, attrs):

        raw_photo = attrs.get("picture") or self.initial_data.get("photo")
        if raw_photo:
            attrs["photo"] = self._decode_base64_image(raw_photo)
        attrs.pop("picture", None)
        return attrs


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"